import streamlit as st
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

st.title("Diamond Price Predictor")

with st.form("diamond_form"):
    carat = st.number_input("Carat")
    depth = st.number_input("Depth")
    table = st.number_input("Table")
    x = st.number_input("X")
    y = st.number_input("Y")
    z = st.number_input("Z")
    cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
    color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity", ["SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

    submitted = st.form_submit_button("Predict")

if submitted:
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
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_new_data)

    results = round(pred[0], 2)

    st.write(f"Predicted price: ${results:.2f}")