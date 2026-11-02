
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Real Estate Investment Advisor", layout="wide")

st.title("🏠 Real Estate Investment Advisor")
st.write("Explore properties and estimate investment suitability.")

df = pd.read_csv("dashboard_data.csv")

st.subheader("Property Market Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Properties", f"{len(df):,}")
col2.metric("Average Price (Lakhs)", f"₹{df['Price_in_Lakhs'].mean():.2f}")
col3.metric("Cities", df["City"].nunique())

st.subheader("Explore Properties")

city = st.selectbox("Select City", ["All"] + sorted(df["City"].unique().tolist()))

filtered_df = df if city == "All" else df[df["City"] == city]

st.dataframe(
    filtered_df[["City", "Locality", "Property_Type", "BHK",
                 "Size_in_SqFt", "Price_in_Lakhs"]].head(100),
    use_container_width=True
)


st.subheader("Investment Suitability Prediction")

age = st.number_input("Property Age (Years)", 0, 100, 10)
schools = st.number_input("Nearby Schools", 0, 50, 5)
hospitals = st.number_input("Nearby Hospitals", 0, 50, 5)
transport = st.selectbox(
    "Public Transport Accessibility",
    ["High", "Medium", "Low"]
)
amenities = st.number_input("Number of Amenities", 0, 20, 3)

if st.button("Check Investment Suitability"):
    model = joblib.load("investment_classifier.pkl")
    features = joblib.load("investment_features.pkl")

    input_data = pd.DataFrame([{
        "Age_of_Property": age,
        "Nearby_Schools": schools,
        "Nearby_Hospitals": hospitals,
        "Amenities_Count": amenities,
        "Public_Transport_Accessibility_High": int(transport == "High"),
        "Public_Transport_Accessibility_Low": int(transport == "Low"),
        "Public_Transport_Accessibility_Medium": int(transport == "Medium")
    }])

    input_data = input_data.reindex(columns=features, fill_value=0)
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Good Investment Suitability")
    else:
        st.warning("Lower Investment Suitability")

    st.caption("Based on a rule-based suitability score, not actual investment returns.")


st.subheader("Five-Year Property Price Estimate")

current_price = st.number_input(
    "Current Property Price (₹ Lakhs)",
    min_value=1.0,
    value=100.0
)

growth_rate = st.slider(
    "Assumed Annual Appreciation (%)",
    min_value=0,
    max_value=15,
    value=5
)

future_price = current_price * (1 + growth_rate / 100) ** 5

if st.button("Calculate Future Price"):
    st.metric("Estimated Price After 5 Years", f"₹{future_price:.2f} Lakhs")
    st.caption("Illustrative scenario only; future market prices are uncertain.")


st.subheader("Filter Properties by Budget and BHK")

max_price = st.slider(
    "Maximum Budget (₹ Lakhs)",
    10, 500, 250
)

bhk = st.selectbox(
    "Select BHK",
    ["All"] + sorted(df["BHK"].unique().tolist())
)

filtered = filtered_df[
    filtered_df["Price_in_Lakhs"] <= max_price
]

if bhk != "All":
    filtered = filtered[filtered["BHK"] == bhk]

st.write("Matching Properties:", len(filtered))

st.dataframe(
    filtered[["City", "Locality", "BHK",
              "Size_in_SqFt", "Price_in_Lakhs"]].head(100)
)


st.subheader("Property Market Insights")

avg_prices = (
    df.groupby("City")["Price_in_Lakhs"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.write("Top 10 Cities by Average Property Price")
st.bar_chart(avg_prices)

st.write("Property Type Distribution")
st.bar_chart(df["Property_Type"].value_counts())
