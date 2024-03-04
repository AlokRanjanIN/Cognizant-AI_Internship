---

# Cognizant AI Internship - Task 3

## Model Building and Interpretation for Gala Groceries

### Overview

Welcome to Task 3 of the Cognizant AI Internship! 📈 This project focuses on building a predictive model using sample data provided by Gala Groceries. From combining, transforming, and modeling datasets to presenting results back to the business, delve into the world of machine learning to develop insights and strategies for smarter stock management and procurement.

### 🔍 Task Details

#### 1. Building a Predictive Model

Build a predictive model using sample data provided by the client.

#### 2. Combining, Transforming, and Modeling Datasets

Combine, transform, and model three datasets in a suitable way to answer the problem statement provided by the business.

#### 3. Communicating Results

Communicate your work and analysis in the form of a PowerPoint slide to present the results back to the business.

### 📋 Task Background

Having outlined the strategic plan for completing the modeling work based on the problem statement.

The client has provided three datasets, and it's our job to combine, transform, and model these datasets in a suitable way to answer the problem statement. Then, we need to communicate our work and analysis in the form of a single PowerPoint slide, ensuring that we use business-friendly language and explain our results in a way that the business will understand.

### 🧩 Modelling Notebook

The notebook contains detailed steps on data cleaning, merging datasets, feature engineering, preprocessing, model building, and visualizing important features.

#### 1. Import Libraries & Load Data

- Imported necessary libraries and loaded the provided datasets: sales, sensor stock levels, and sensor storage temperature.

#### 2. Data Cleaning

- Performed data cleaning tasks such as dropping unnecessary columns, converting timestamp to datetime format, handling missing values, and verifying data integrity.

#### 3. Merge Datasets

- Merged datasets based on common columns like `timestamp` and `product_id` to create a comprehensive dataset for modeling.

#### 4. Feature Engineering

- Engineered features including day of month, day of week, and hour from the timestamp column.
- Applied one-hot encoding (OHE) to categorical variables.

#### 5. Preprocessing

- Split the data into training and testing sets.
- Standardized numerical features using StandardScaler.

#### 6. Model Building

- Utilized CatBoost, XGBoost, Random Forest Regression, Support Vector Regression, and Mean of y_train for modeling.
- Evaluated models using cross-validation score and evaluation metrics such as mean absolute error, mean squared error, and adjusted R-squared.

#### 7. Visualize Important Features

- Plotted relative feature importances from the CatBoost model.
- Analyzed feature coefficients from the Lasso model.
- Visualized feature correlation with the target variable.

### 📊 PowerPoint Presentation

- Presented a summary of the problem statement and model selection.
- Communicated model performance and results summary.
- Included a bar graph of relative feature importances for each feature.

### 🖥️ How to Review

1. Clone the Repository.
2. Navigate to the Task 3 Directory.
3. Explore the notebook content for detailed modeling steps.
4. Review the PowerPoint slide for a summary of results and conclusions.

### 📝 Note

Please refrain from directly copying the internship task code for commercial purposes. This repository is for educational purposes only. Use the code wisely and responsibly, and strive to understand the concepts and methodologies behind the analysis.

### Conclusion

Task 3 focuses on building a predictive model and interpreting the results back to the business for smarter stock management and procurement at Gala Groceries. By leveraging the provided datasets and implementing machine learning algorithms, we aim to develop actionable insights and strategies to improve stock level predictions and enhance procurement practices.

---

Feel free to explore the provided modeling notebook and PowerPoint presentation further to gain deeper insights into Gala Groceries' predictive modeling and interpretation strategies for stock management and procurement! 📊🛒
