from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
import time

# Inject custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #121212; /* Dark theme background */
        color: #ffffff;
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
        color: #90EE90;
    }
    </style>
""", unsafe_allow_html=True)

# Load Keras model only once
@st.cache_resource
def load_bamboo_model():
    return load_model("bamboo_growth_model.h5", compile=False)

model = load_bamboo_model()

st.title("🎍 Bamboo Growth Prediction App")

# Inputs
val1 = st.number_input("Rainfall (mm)", value=100.0)
val2 = st.number_input("Temperature (°C)", value=25.0)
val3 = st.number_input("Soil pH", value=6.5)
val4 = st.number_input("Sunlight Hours", value=8.0)
val5 = st.number_input("Fertilizer Used (kg)", value=2.0)

# Initialize session state
if "prediction" not in st.session_state:
    st.session_state.prediction = None

if st.button("Generate Prediction"):
    features = np.array([[val1, val2, val3, val4, val5]])

    # Simulate loading bar
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    # Predict safely
    try:
        prediction = model.predict(features, verbose=0)
        st.session_state.prediction = prediction[0][0]
    except Exception as e:
        st.error(f"⚠️ Error while predicting: {e}")

# Show result if available
if st.session_state.prediction is not None:
    st.im

