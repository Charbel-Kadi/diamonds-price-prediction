import streamlit as st
import requests

st.title("Diamond Price Prediction")

carat = st.number_input("Carat", min_value=0.1, max_value=10.0, step=0.1)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])
depth = st.number_input("Depth", min_value=40.0, max_value=80.0, step=0.1)
table = st.number_input("Table", min_value=40.0, max_value=100.0, step=0.1)
x = st.number_input("Length (x)", min_value=0.0, max_value=15.0, step=0.1)
y = st.number_input("Width (y)", min_value=0.0, max_value=15.0, step=0.1)
z = st.number_input("Depth (z)", min_value=0.0, max_value=15.0, step=0.1)

if st.button("Predict Price"):
    input_data = {
        "carat": carat,
        "cut": cut,
        "color": color,
        "clarity": clarity,
        "depth": depth,
        "table": table,
        "x": x,
        "y": y,
        "z": z
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
    prediction = response.json()["predicted_price"]
    st.success(f"💎 Predicted Diamond Price: ${prediction}")