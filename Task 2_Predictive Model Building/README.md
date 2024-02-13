---

# British Airways Internship - Task 2

## BA Customer Booking Prediction

### Overview

Welcome to Task 2 of the British Airways Internship! In this task, we delve into the fascinating world of predictive modeling to understand customer booking behavior. By leveraging advanced machine learning techniques, we aim to uncover the key factors influencing booking decisions, empowering British Airways to tailor its services and offerings effectively.

### 🔍 Code Overview

#### 1. Importing Libraries

We start by importing essential libraries for data manipulation, visualization, and machine learning.

#### 2. Importing Dataset

The dataset (`customer_booking.csv`) is loaded into a Pandas DataFrame for comprehensive analysis.

#### 3. Exploratory Data Analysis (EDA)

We dive into exploratory data analysis to gain insights into the dataset, visualize key features, and understand their distributions.

#### 4. Pre-processing

Prepare the dataset for modeling by handling categorical variables, exploring unique values, and splitting the data into training and testing sets.

#### 5. Model Training - CatBoost

Train a powerful CatBoostClassifier, evaluate its performance, and visualize key metrics and confusion matrices.

#### 6. Model Training - XGBoost

Utilize XGBoost to train a robust model with different configurations, including default settings, validation sets, and hyperparameter tuning.

#### 7. Evaluation Metrics

Assess model performance using essential evaluation metrics such as accuracy, F1 score, precision, recall, and ROC-AUC.

#### 8. XGBoost Feature Importance

Visualize the top feature importances from the tuned XGBoost model to understand the most influential factors.

### 💻 How to Use

1. Clone the Repository.
2. Navigate to the Project Directory.
3. Explore the Task 2 Notebook.
4. Run the Notebook Cells.


### 🛠️ Dependencies

#### Required Libraries:

- Pandas
- NumPy
- Matplotlib
- Plotly
- Seaborn
- XGBoost
- CatBoost
- Scikit-learn
- Imbalanced-learn
- Bayesian optimization (skopt)

### 📝 Note

Please refrain from directly copying the internship task code for commercial purposes. This repository is for educational purposes only. Use the code wisely and responsibly, and strive to understand the concepts and methodologies behind the analysis.

### Performance Metrics of Final Tuned XGBoost Classifier Model

| Metric     | On Train Set (%) | On Test Set (%) |
|------------|------------------|-----------------|
| Accuracy   | 85.346           | 72.435          |
| F1         | 86.101           | 71.140          |
| Precision  | 81.885           | 74.649          |
| Recall     | 90.774           | 67.946          |
| ROC_AUC    | 93.499           | 80.286          |

### Conclusion

Task 2 of the British Airways Internship has unveiled crucial insights into customer booking behavior. Leveraging advanced machine learning techniques, we've identified key factors influencing booking decisions. Our tuned XGBoost model demonstrates high accuracy and precision, equipping British Airways with valuable predictive capabilities.

---

Let's continue our exploration of customer behavior with data-driven insights! ✨🚀
