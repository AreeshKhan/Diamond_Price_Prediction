## Getting Started

### Training Pipeline

To run the training pipeline, execute the following command in your terminal:
`python src/pipelines/training_pipeline.py`

### Flask App

The Flask app code is located in `app.py`. To run the app, execute the following command:
`python app.py`

The app will be available at the following local host address:
`http://127.0.0.1:5000/`


### Streamlit App

The Streamlit app code is located in `main.py`. To run the app, execute the following command:
`streamlit run main.py`
The Streamlit live web app for Diamond Price Prediction:
Link: `https://areesh-khan-diamond-price-prediction.streamlit.app/`
### Note

You can uncomment line 45 in `Model_trainer.py` for a better Regressor Model.
However, please note that I couldn't do so due to the pickle file size exceeding the Git upload size limit.
