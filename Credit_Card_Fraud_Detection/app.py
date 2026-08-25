import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_model.pkl")

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details to check whether it is Fraud or Genuine.")

# Input fields

transaction_id = st.text_input("Transaction ID")
amount_usd = st.number_input("Transaction Amount (USD)")

merchant_category = st.text_input("Merchant Category")
card_type = st.text_input("Card Type")
auth_method = st.text_input("Authentication Method")
channel = st.text_input("Channel")
device_type = st.text_input("Device Type")

is_foreign_transaction = st.selectbox(
    "Foreign Transaction",
    [0, 1]
)

hours_since_last_txn = st.number_input("Hours Since Last Transaction")
txn_count_last_24h = st.number_input("Transaction Count Last 24 Hours")

distance_from_home_km = st.number_input("Distance From Home (km)")
card_age_months = st.number_input("Card Age (Months)")
customer_age = st.number_input("Customer Age")

account_balance_usd = st.number_input("Account Balance (USD)")

is_new_merchant = st.selectbox(
    "New Merchant",
    [0, 1]
)

used_vpn = st.selectbox(
    "Used VPN",
    [0, 1]
)

ip_country_mismatch = st.selectbox(
    "IP Country Mismatch",
    [0, 1]
)

billing_shipping_mismatch = st.selectbox(
    "Billing Shipping Mismatch",
    [0, 1]
)

cvv_retry_count = st.number_input("CVV Retry Count")

velocity_score = st.number_input("Velocity Score")

time_of_day_hour = st.number_input("Hour of Day")

day_of_week = st.number_input("Day of Week")

is_ai_generated_scam_attempt = st.selectbox(
    "AI Generated Scam Attempt",
    [0, 1]
)

merchant_risk_score = st.number_input("Merchant Risk Score")

prior_disputes = st.number_input("Prior Disputes")


# Prediction button

if st.button("Predict"):

    input_data = pd.DataFrame({
        "transaction_id":[transaction_id],
        "amount_usd":[amount_usd],
        "merchant_category":[merchant_category],
        "card_type":[card_type],
        "auth_method":[auth_method],
        "channel":[channel],
        "device_type":[device_type],
        "is_foreign_transaction":[is_foreign_transaction],
        "hours_since_last_txn":[hours_since_last_txn],
        "txn_count_last_24h":[txn_count_last_24h],
        "distance_from_home_km":[distance_from_home_km],
        "card_age_months":[card_age_months],
        "customer_age":[customer_age],
        "account_balance_usd":[account_balance_usd],
        "is_new_merchant":[is_new_merchant],
        "used_vpn":[used_vpn],
        "ip_country_mismatch":[ip_country_mismatch],
        "billing_shipping_mismatch":[billing_shipping_mismatch],
        "cvv_retry_count":[cvv_retry_count],
        "velocity_score":[velocity_score],
        "time_of_day_hour":[time_of_day_hour],
        "day_of_week":[day_of_week],
        "is_ai_generated_scam_attempt":[is_ai_generated_scam_attempt],
        "merchant_risk_score":[merchant_risk_score],
        "prior_disputes":[prior_disputes]
    })


prediction = model.predict(input_data)
probability = model.predict_proba(input_data)

    if prediction[0] == 1:
    st.error("⚠️ Fraudulent Transaction Detected")
    st.write("Fraud Probability:", round(probability[0][1]*100, 2), "%")
else:
    st.success("✅ Genuine Transaction")
    st.write("Genuine Probability:", round(probability[0][0]*100, 2), "%")