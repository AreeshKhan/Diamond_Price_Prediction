import streamlit as st
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline
import pickle
import pandas as pd

# Load models and vectorizer
preprocessor = pickle.load(open('artifacts/preprocessor.pkl', 'rb'))
model = pickle.load(open('artifacts/model.pkl', 'rb'))

# Title for the app
st.title("Diamond Price Prediction")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict"])

# Home page
if page == "Home":
    st.header("Welcome!")
    st.write("Want to check your diamond's price?")
    st.write("Navigate to the Predict page using the sidebar.")

# Prediction page
if page == "Predict":
    st.header("Diamond Price Prediction Form")

    # Form inputs
    carat = st.number_input("Carat", min_value=0.0, format="%.2f")
    depth = st.number_input("Depth", min_value=0.0, format="%.2f")
    table = st.number_input("Table", min_value=0.0, format="%.2f")
    x = st.number_input("x", min_value=0.0, format="%.2f")
    y = st.number_input("y", min_value=0.0, format="%.2f")
    z = st.number_input("z", min_value=0.0, format="%.2f")

    cut = st.selectbox("Cut", options=["Fair", "Good", "Very Good", "Premium", "Ideal"])
    color = st.selectbox("Color", options=["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity", options=["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

    # Prediction button
    if st.button("Predict"):
        try:
            # Collect data
            data = CustomData(
                carat=carat,
                depth=depth,
                table=table,
                x=x,
                y=y,
                z=z,
                cut=cut,
                color=color,
                clarity=clarity
            )
            final_new_data = data.get_data_as_dataframe()

            # Debug: Print the prepared data
            st.write("Prepared Data:")
            st.write(final_new_data)

            new_data_scaled = preprocessor.transform(final_new_data)
            # Make predictions
            result = model.predict(new_data_scaled)

            result = round(result[0], 2)

            # Display result
            st.success(f"Your Predicted Diamond Price: {result} USD")

        except Exception as e:
            # Display error message
            st.error("An error occurred during prediction.")
            st.error(f"Error Details: {str(e)}")
