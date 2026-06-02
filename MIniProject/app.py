import streamlit as st
import numpy as np
import joblib
import datetime

# Load model
model = joblib.load("pending_model.pkl")

# Page Title
st.title("🚦 Pending Challan Prediction System")
st.subheader("Machine Learning Model — SDG Goal 16 (Peace, Justice & Strong Institutions)")

st.write("""
This system predicts **pending challans for a given day** based on challan activity recorded on that day.  
It helps traffic departments forecast workload and manage backlog efficiently.
""")

# Sidebar Input Form
st.sidebar.header("📥 Enter Challan Details")

totalChallan = st.sidebar.number_input("Total Challans Issued Today", min_value=0)
disposedChallan = st.sidebar.number_input("Disposed Challans Today", min_value=0)
pendingAmount = st.sidebar.number_input("Pending Amount Today", min_value=0)
disposedAmount = st.sidebar.number_input("Disposed Amount Today", min_value=0)
totalAmount = st.sidebar.number_input("Total Amount Today", min_value=0)

pendingCourt = st.sidebar.number_input("Pending Court Cases Today", min_value=0)
disposedCourt = st.sidebar.number_input("Disposed Court Cases Today", min_value=0)
totalCourt = st.sidebar.number_input("Total Court Cases Today", min_value=0)

date = st.sidebar.date_input("Select Date", datetime.date.today())

# Extract date features
day = date.day
month = date.month
year = date.year
day_of_week = date.weekday()
is_weekend = 1 if day_of_week >= 5 else 0

# Prediction Button
if st.sidebar.button("Predict Pending Challans"):
    input_array = np.array([[totalChallan, disposedChallan,
                             pendingAmount, disposedAmount, totalAmount,
                             pendingCourt, disposedCourt, totalCourt,
                             day, month, year, day_of_week, is_weekend]])
    
    prediction = int(model.predict(input_array)[0])
    
    st.success(f"📌 Predicted Pending Challans for this day: **{prediction}**")

    # Interpretation Messages
    if prediction > 50000:
        st.warning("⚠ High backlog expected. Additional staff may be required.")
    elif prediction > 20000:
        st.info("📊 Moderate backlog. Timely disposal is recommended.")
    else:
        st.success("✅ Backlog is under control.")