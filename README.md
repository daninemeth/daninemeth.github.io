# Data Science portfolio by Daniel Nemeth

I’ve been an e-commerce professional at one of Hungary’s largest fast fashion stores for 5 years. As a leader, a big part of my day-to-day job was analyzing the data related to sales, complaints, reviews, customer service KPIs, and communicating them to the other departments. In order to be more proficient, I pursued an education in statistics, programming, data science, and machine learning. Now I am looking to pivot to a more technical role. [Contact me](mailto:dnemeth@mailbox.org)

## Tech Stack

* **Programming:**      Python
* **Data Science:**     NumPy, SciPy, pandas, matplotlib, Seaborn, Excel, PowerBI
* **Machine Learning:** scikit-learn
* **Databases:**        SQL (PostgreSQL)
* **Misc.:**            Linux (bash), git, JIRA, Postman

## Projects

### Stock Screener

In this project there is a python script which takes in a dataframe of stock market symbols, downloads the latest financial data using the yfinance library, and writes it to a csv file. We will do exploratory data analysis on the resultant dataframe, and use value investing principles inspired by prof. Damodaran's NYU course and Joel Greenblatt's *The Little Book That Beats the Market* as guides to filter down the most undervalued companies by sector. (yfinance, NumPy, pandas, seaborn) [Link](https://github.com/daninemeth/daninemeth.github.io/tree/main/stock_screener)

### Telco Churn prediction

An exploratory data analysis and some feature engineering on a telecom customer dataset. Then in the second part of the Jupyter Notebook I execute different tree based machine learning algorithms to predict whether a customer will cancel anytime soon. The methods implemented are: **Decision Tree, Random Forest, AdaBoost, and Gradient Boosting**, and then I compared their performance against each other. (NumPy, pandas, seaborn, scikit-learn) [Link](https://github.com/daninemeth/daninemeth.github.io/tree/main/churn_prediction)

### Sesame Street and Cognitive Development

This project is a reproduction of the classic developmental psychology study on the Sesame Street tv show. We will explore the data, create new columns for the changes in cognitive abilities, and we'll do a **two sample t test** on the change in literacy among the regular viewers. At the end of the notebook I linearly regress the data tho determine the most important coefficients. (Numpy, SciPy, pandas, seaborn, scikit-learn) [Link](https://github.com/daninemeth/daninemeth.github.io/tree/main/sesame_street_cognition)

### Civil War prediction using econometrics

This is a replication of an Oxford econometric study from 2004 by Paul Collier and Anke Hoeffler *(Greed and grievance in civil war, Oxford Economic Papers 56, (2004), 563-595)*.  In the Jupyter Notebook I analyze the data, impute where deemed necessary, and use a class weighted **logistic regression** algorithm to predict the probability of a civil war breaking out in the following 5 year period, then analyze the most important coefficients. (NumPy, pandas, seaborn, scikit-learn) [Link](https://github.com/daninemeth/daninemeth.github.io/tree/main/civil_wars)
