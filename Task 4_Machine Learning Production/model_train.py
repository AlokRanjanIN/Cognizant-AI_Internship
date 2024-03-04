import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Define file paths for data files
SALES_FILE = "sales.csv"
STOCK_FILE = "sensor_stock_levels.csv"
TEMP_FILE = "sensor_storage_temperature.csv"

def load_data(sales_file, stock_file, temp_file):
    """
    Load data from CSV files into Pandas DataFrames.
    
    Args:
        sales_file (str): Path to the sales data CSV file.
        stock_file (str): Path to the stock data CSV file.
        temp_file (str): Path to the temperature data CSV file.
    
    Returns:
        tuple: Tuple containing three Pandas DataFrames for sales, stock, and temperature data.
    """
    sales_df = pd.read_csv(sales_file)
    stock_df = pd.read_csv(stock_file)
    temp_df = pd.read_csv(temp_file)
    return sales_df, stock_df, temp_df

def clean_data(sales_df, stock_df, temp_df):
    """
    Clean the data by dropping unnecessary columns and handling missing values.
    
    Args:
        sales_df (DataFrame): DataFrame containing sales data.
        stock_df (DataFrame): DataFrame containing stock data.
        temp_df (DataFrame): DataFrame containing temperature data.
    
    Returns:
        tuple: Tuple containing cleaned sales, stock, and temperature DataFrames.
    """
    # Drop unnecessary columns
    dfs = [sales_df, stock_df, temp_df]
    for df in dfs:
        df.drop(columns=["Unnamed: 0"], inplace=True, errors='ignore')
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S').dt.round('h')
        df['quantity'] = df['quantity'].fillna(0)  # Fill missing values with 0 for 'quantity' column
    return sales_df, stock_df, temp_df

def merge_datasets(sales_df, stock_df, temp_df):
    """
    Merge the cleaned sales, stock, and temperature DataFrames.
    
    Args:
        sales_df (DataFrame): Cleaned DataFrame containing sales data.
        stock_df (DataFrame): Cleaned DataFrame containing stock data.
        temp_df (DataFrame): Cleaned DataFrame containing temperature data.
    
    Returns:
        DataFrame: Merged DataFrame containing aggregated data.
    """
    sales_agg = sales_df.groupby(['timestamp','product_id']).agg({'quantity':'sum'}).reset_index()
    stock_agg = stock_df.groupby(['timestamp','product_id']).agg({'estimated_stock_pct':'mean'}).reset_index()
    merge_df = sales_agg.merge(stock_agg, how='right', on=['timestamp','product_id'])
    merge_df['quantity'] = merge_df['quantity'].fillna(0)
    temp_agg = temp_df.groupby(['timestamp']).agg({'temperature':'mean'}).reset_index()
    merge_df = merge_df.merge(temp_agg, how='left', on=['timestamp'])
    product_details = sales_df[['product_id','category','unit_price']].drop_duplicates()
    merge_df = merge_df.merge(product_details, how='left', on='product_id')
    return merge_df

def feature_engineering(merge_df):
    """
    Perform feature engineering on the merged DataFrame.
    
    Args:
        merge_df (DataFrame): Merged DataFrame containing aggregated data.
    
    Returns:
        DataFrame: DataFrame with engineered features.
    """
    final_df = merge_df.copy()
    final_df['day_of_month'] = final_df['timestamp'].dt.day.astype('uint8')
    final_df['day_of_week'] = final_df['timestamp'].dt.day_of_week.astype('uint8')
    final_df['hour'] = final_df['timestamp'].dt.hour.astype('uint8')
    final_df.drop(columns=['timestamp'], inplace=True)
    cat_columns = ['product_id','category']
    final_df[cat_columns] = final_df[cat_columns].astype('category')
    return final_df

def preprocess_data(final_df):
    """
    Preprocess the final DataFrame for modeling.
    
    Args:
        final_df (DataFrame): DataFrame with engineered features.
    
    Returns:
        tuple: Tuple containing preprocessed X_train, X_test, y_train, and y_test.
    """
    X = final_df.drop(columns=['estimated_stock_pct'], axis=1)
    y = final_df['estimated_stock_pct']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    std_scaler = StandardScaler()
    non_cat_col = [idx for idx, dtype in enumerate(X.dtypes) if dtype.kind in ['i', 'u', 'f']]
    X_train.iloc[:,non_cat_col] = std_scaler.fit_transform(X_train.iloc[:,non_cat_col])
    X_test.iloc[:,non_cat_col] = std_scaler.transform(X_test.iloc[:,non_cat_col])
    return X_train, X_test, y_train, y_test

def train_catboost(X_train, y_train):
    """
    Train a CatBoost regressor model.
    
    Args:
        X_train (array-like): Training features.
        y_train (array-like): Training target.
    
    Returns:
        CatBoostRegressor: Trained CatBoost model.
    """
    cat_columns = [col for col in X_train.select_dtypes('category').columns]
    catboost_reg = CatBoostRegressor(cat_features=cat_columns, verbose=False, random_state=42)
    catboost_reg.fit(X_train, y_train)
    return catboost_reg

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the performance of the model on the test data.
    
    Args:
        model: Trained regression model.
        X_test (array-like): Test features.
        y_test (array-like): Test target.
    
    Returns:
        dict: Dictionary containing evaluation metrics.
    """
    y_pred = model.predict(X_test)
    n = y_test.shape[0]
    p = X_test.shape[1]
    
    metrics = {
        'MAE': mean_absolute_error(y_test, y_pred),
        'MSE': mean_squared_error(y_test, y_pred),
        'R2 Score': r2_score(y_test, y_pred),
        'Adjusted R2 Score': 1 - (1 - r2_score(y_test, y_pred)) * (n - 1) / (n - p - 1)
    }
    return metrics

def visualize_feature_importance(model, X):
    """
    Visualize the feature importances of the model.
    
    Args:
        model: Trained regression model.
        X (DataFrame): Features.
    """
    features = [i for i in X.columns]
    importances = model.feature_importances_
    indices = np.argsort(importances)
    plt.figure(figsize=(5,6))
    plt.title('Relative Feature Importances (By CatBoost)')
    plt.barh(range(len(indices)), importances[indices], color='lightgreen', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.show()

# Example usage:
if __name__ == "__main__":
    # Load data   
    sales_df, stock_df, temp_df = load_data(SALES_FILE, STOCK_FILE, TEMP_FILE)
        
    # Clean data
    sales_df, stock_df, temp_df = clean_data(sales_df, stock_df, temp_df)
        
    # Merge datasets
    merge_df = merge_datasets(sales_df, stock_df, temp_df)

    # Perform feature engineering
    final_df = feature_engineering(merge_df)
    
    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(final_df)
    
    # Train CatBoost model
    catboost_reg = train_catboost(X_train, y_train)
    
    # Evaluate model
    metrics = evaluate_model(catboost_reg, X_test, y_test)
    print("CatBoost Model Metrics:")
    print(metrics)

    # Visualize feature importance
    visualize_feature_importance(catboost_reg, final_df.drop(columns=['estimated_stock_pct']))

