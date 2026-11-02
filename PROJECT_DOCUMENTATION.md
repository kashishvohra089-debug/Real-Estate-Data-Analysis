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
