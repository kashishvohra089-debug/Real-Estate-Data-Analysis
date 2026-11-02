# Real Estate Investment Advisor

## Project Objective
Analyze real estate data and build an interactive
application to explore property investment suitability.

## Dataset
250,000 properties across 42 Indian cities.

## Tools Used
Python, Pandas, Scikit-learn, MLflow and Streamlit.

## Features
- Property market overview
- City, budget and BHK filters
- Investment suitability classification
- Five-year price scenario estimation
- Property market visualizations

## Important Limitations
Investment suitability is based on defined scoring rules,
not observed investment returns.

The five-year estimate uses an assumed annual growth rate,
not a machine-learning forecast trained on historical prices.

## How to Run
Install dependencies:
pip install -r requirements.txt

Start the application:
streamlit run app.py

## Methodology

1. **Data Collection:** Used a real estate dataset containing 250,000 property records from 42 Indian cities.
2. **Data Cleaning:** Checked missing values, duplicates, and inconsistent property information.
3. **Exploratory Data Analysis:** Studied property prices, locations, property types, sizes, nearby facilities, and other factors using Python visualizations.
4. **Feature Engineering:** Created additional features such as property age, amenities count, and floor ratio.
5. **Machine Learning:** Trained regression models to study property price prediction and a Random Forest classification model to estimate investment suitability.
6. **Model Evaluation:** Used evaluation metrics to examine model performance and MLflow to record the investment classification experiment.
7. **Dashboard Development:** Built an interactive Streamlit application to explore properties, check investment suitability, and estimate five-year property values.

## Findings

- The dataset contains approximately 250,000 property records covering 42 Indian cities.
- The average property price is approximately ₹254.59 lakhs.
- Property prices vary across cities, localities, and property types.
- The analysis of nearby schools showed little difference in average price per square foot across the groups.
- The property price regression models showed limited predictive performance, indicating that the available features did not explain price variation well.
- The investment classification model achieved 100% accuracy on the test data. This unusually high result requires further validation to rule out data leakage or an overly simple rule-based target.
- The five-year property value estimate uses an assumed annual appreciation rate rather than a model validated against actual future prices.

## Use Cases

1. **Property Buyers:** Explore property information and compare prices across different cities.
2. **Real Estate Investors:** Examine property characteristics and obtain an indicative investment suitability assessment.
3. **Real Estate Analysts:** Study market patterns, property prices, and factors associated with property values.
4. **Property Price Planning:** Estimate possible property values after five years using different assumed appreciation rates.
5. **Interactive Decision Support:** Use the Streamlit dashboard to explore properties and view investment-related information.

**Note:** The predictions and estimates are intended for educational and analytical purposes. They should not be treated as guaranteed investment outcomes or professional financial advice.
