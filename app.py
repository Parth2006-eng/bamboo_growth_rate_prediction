from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
import time
# Inject custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to right, #e6f9f0, #ffffff);
    }
    .stButton>button {
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #388E3C;
        transform: scale(1.05);
    }
    .css-10trblm {
        font-weight: bold;
        color: #1B5E20;
    }
    </style>
""", unsafe_allow_html=True)
dark_theme_css = """
<style>
    body {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .css-1d391kg, .css-18e3th9 {
        background-color: #262730;
        color: #FFFFFF;
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: #FFFFFF !important;
    }
    .stButton button {
        background-color: #1DB954;
        color: #FFFFFF;
        border-radius: 8px;
        border: none;
    }
    .stButton button:hover {
        background-color: #14833b;
        color: #FFFFFF;
    }
</style>

# Load Keras model without compiling (ignores optimizer/loss/metrics)
model = load_model("bamboo_growth_model.h5", compile=False)

st.title("🎍 Bamboo Growth Prediction App")

# Inputs
val1 = st.number_input("Rainfall (mm)", value=100.0)
val2 = st.number_input("Temperature (°C)", value=25.0)
val3 = st.number_input("Soil pH", value=6.5)
val4 = st.number_input("Sunlight Hours", value=8.0)
val5 = st.number_input("Fertilizer Used (kg)", value=2.0)

if st.button("Generate Prediction"):
    features = np.array([[val1, val2, val3, val4, val5]])

    # Simulate loading bar (5 seconds)
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress.progress(i + 1)

    # Predict
    prediction = model.predict(features)

    
    st.image("https://cdn.dribbble.com/userupload/21899904/file/original-c8a4ed87f00c7f1fb5d056ba0e5ff502.gif", caption="Prediction Result", use_container_width=True)
    st.success(f"🌱 Predicted Growth: {prediction[0][0]:.2f} cm/month")
