---

# Cognizant AI Internship - Task 2

## Data Modeling for Gala Groceries

### Overview

Welcome to Task 2 of the Cognizant AI Internship! 🛒 This project focuses on understanding relational data and framing a problem statement for Gala Groceries. From reviewing data model diagrams to creating strategic plans, delve into the depths of data modeling to develop insights and strategies for predictive analysis and inventory optimization.

### 🔍 Task Details

#### 1. Understanding Relational Data

Develop an understanding of relational data and how to frame a problem statement.

#### 2. Reviewing Data Model Diagram

Review a data model diagram provided by the Data Engineering team and create a strategic plan on how to use this data to answer the problem statement.

#### 3. Strategic Plan Presentation

Summarize the choices and plan of work in a PowerPoint presentation, which will be reviewed by the Data Science team leader and the client.

### 📋 Task Background

My work on the previous task has been instrumental in propelling this project forward with the client. Based on my recommendations, the client wants to focus on the following problem statement:

“Can we accurately predict the stock levels of products based on sales data and sensor data on an hourly basis in order to more intelligently procure products from our suppliers?”

The client has agreed to share more data in the form of sensor data, including temperature measurements from storage facilities and estimated stock levels from sensors in refrigerators and freezers. 

### 🛠️ Data Model Diagram

#### 1. Sales Table

Contains sales data with columns:
- transaction_id
- timestamp
- product_id
- category
- customer_type
- unit_price
- quantity
- total
- payment_type

#### 2. Sensor Storage Temperature Table

Contains IoT data from temperature sensors in the storage facility with columns:
- id
- timestamp
- temperature

#### 3. Sensor Stock Levels Table

Contains estimated stock levels of products based on IoT sensors with columns:
- id
- timestamp
- product_id
- estimated_stock_pct

### 💼 Strategic Plans

#### Objective

Accurately predict hourly product stock levels using sales and sensor data.

#### Approach

1. **Data Utilization**: Utilize sales data for historical trends and sensor data for real-time warehouse monitoring.
2. **Data Quality Assurance**: Ensure data integrity, handle missing values, and identify outliers for a reliable dataset.
3. **Feature Engineering**: Extract relevant features for model building.
4. **Exploratory Data Analysis (EDA)**: Analyze dataset patterns, correlations, and anomalies.
5. **Model Building**: Train predictive model using historical data.
6. **Predictive Analysis**: Use trained model for hourly stock level predictions.
7. **Inventory Optimization**: Develop a data-driven strategy aligned for efficient resource utilization and minimized wastage.
8. **Iterative Refinement**: Continuously refine model and strategies based on performance metrics for operational excellence in stock management.

### 🖥️ How to Review

1. Clone the Repository.
2. Navigate to the Task 2 Directory.
3. Explore the provided data model diagram and strategic plan presentation.

### 📝 Note

Please refrain from directly copying the internship task code for commercial purposes. This repository is for educational purposes only. Use the code wisely and responsibly, and strive to understand the concepts and methodologies behind the analysis.

### Conclusion

Task 2 focuses on understanding relational data and creating a strategic plan for predictive analysis and inventory optimization at Gala Groceries. By leveraging the provided data model diagram and strategic plan presentation, the Data Science team can develop actionable insights and strategies to enhance stock management practices.

---

Feel free to explore the provided data model diagram and strategic plan presentation further to gain deeper insights into Gala Groceries' data modeling and predictive analysis strategies! 🛒📊
