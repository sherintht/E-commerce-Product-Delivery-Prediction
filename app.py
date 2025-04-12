import streamlit as st
import pandas as pd
import joblib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load trained model and scaler
model = joblib.load(r"D:\python\john_test\best_model.joblib")
scaler = joblib.load(r"D:\python\john_test\scaler.joblib")

# Streamlit UI
st.title("E-commerce Product Delivery Prediction")
st.write("Predict whether a product will be delivered on time.")

# User input fields

warehouse_block = st.selectbox("Warehouse Block", ["A", "B", "C", "D", "E"])
mode_of_shipment = st.selectbox("Mode of Shipment", ["Ship", "Flight", "Road"])
customer_care_calls = st.number_input("Customer Care Calls", min_value=0, max_value=10, step=1)
customer_rating = st.number_input("Customer Rating", min_value=1, max_value=5, step=1)
cost_of_product = st.number_input("Cost of the Product", min_value=1, step=1)
prior_purchases = st.number_input("Prior Purchases", min_value=0, step=1)
product_importance = st.selectbox("Product Importance", ["low", "medium", "high"])
gender = st.selectbox("Customer Gender", ["Male", "Female"])
discount_offered = st.number_input("Discount Offered", min_value=0, step=1)
weight_in_gms = st.number_input("Weight in Grams", min_value=1, step=1)

# Encode categorical values
encoder_dict = {
    "warehouse_block": {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4},
    "mode_of_shipment": {"Ship": 0, "Flight": 1, "Road": 2},
    "product_importance": {"low": 0, "medium": 1, "high": 2},
    "gender": {"Male": 0, "Female": 1}
}

input_data = np.array([
    
    encoder_dict["warehouse_block"][warehouse_block],
    encoder_dict["mode_of_shipment"][mode_of_shipment],
    customer_care_calls,
    customer_rating,
    cost_of_product,
    prior_purchases,
    encoder_dict["product_importance"][product_importance],
    encoder_dict["gender"][gender],
    discount_offered,
    weight_in_gms
]).reshape(1, -1)

# Scale input data
input_data = scaler.transform(input_data)

# Predict
if st.button("Predict Delivery Status"):
    prediction = model.predict(input_data)
    result = "On Time" if prediction[0] == 1 else "Delayed"
    st.write(f"### Prediction: {result}")


