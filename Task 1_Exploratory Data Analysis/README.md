---

# British Airways Internship - Task 1

## BA Customer Review Analysis

### Overview

Welcome to Task 1 of the British Airways Internship! 🛫 This project focuses on analyzing customer reviews of British Airways (BA) gathered from [skytrax](https://www.airlinequality.com/airline-reviews/british-airways). From sentiment analysis to topic modeling, delve into the depths of customer feedback to gain insights into passenger experiences and satisfaction levels.

### 🔍 Code Overview

#### 1. Web Scraping

The code scrapes customer reviews of British Airways from airlinequality.com, collecting various attributes such as aircraft type, traveler type, seat type, country of residence, route, recommended status, overall rating, and more.

#### 2. Cleaning & Preprocessing

After scraping the data, the code performs cleaning and preprocessing tasks, including handling missing values, converting data types, removing duplicates, and splitting the 'route' column into 'from' and 'to' destinations.

#### 3. Exploratory Data Analysis (EDA)

The EDA section provides insights into the dataset through descriptive statistics, visualization of data distributions, correlation analysis, trend analysis, and more. Key visualizations include histograms, box plots, heatmaps, trend plots, and sentiment analysis.

#### 4. Sentiment Analysis

Sentiment analysis is conducted to assess the polarity of customer reviews, categorizing them as positive, neutral, or negative. The code calculates sentiment scores using TextBlob and visualizes sentiment distributions over time.

#### 5. WordCloud of Reviews

Word clouds are generated to visually represent the most frequent words in customer reviews. Separate word clouds are created for all reviews, positive reviews, and negative reviews, offering a glimpse into the most commonly mentioned aspects.

#### 6. Topic Modeling

The code implements topic modeling using Non-negative Matrix Factorization (NMF) to identify prevalent topics in customer reviews. Top words for each topic are displayed, and the distribution of reviews among topics is visualized.

#### 7. Analysis of Reviews After Mid-2022

A specific analysis is performed on negative reviews posted after mid-2022, exploring topics such as connecting flight hassles, business class woes, customer service critique, luggage woes and delays, and culinary and service disappointments.

### 💻 How to Use

1. Clone the Repository.
2. Navigate to the Project Directory.
3. Explore the Task 2 Notebook.
4. Run the Notebook Cells.


### 🛠️ Dependencies

#### Required Libraries:

- requests
- BeautifulSoup
- pandas
- collections
- numpy
- seaborn
- matplotlib
- textblob
- wordcloud
- time
- gensim
- nltk
- sklearn
- plotly
- PIL

### 📝 Note

Please refrain from directly copying the internship task code for commercial purposes. This repository is for educational purposes only. Use the code wisely and responsibly, and strive to understand the concepts and methodologies behind the analysis.

### Conclusion

The BA Customer Review Analysis offers valuable insights into customer sentiments and preferences regarding British Airways services. By understanding the key drivers of customer satisfaction and dissatisfaction, BA can make informed decisions to improve its offerings and enhance the overall passenger experience.

---

Feel free to explore the code and analysis further to gain deeper insights into BA customer feedback! ✈️📊
