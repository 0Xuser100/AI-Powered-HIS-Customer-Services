import streamlit as st
import requests

st.title("Pain & Go Hospital Query System")

# Input for user query
query = st.text_input("Enter your query:")

# Button to submit query
if st.button("Submit Query"):
    response = requests.post("http://localhost:5000/query", json={"query": query})
    if response.status_code == 200:
        st.write("Response:", response.json()["answer"])
    else:
        st.write("Error:", response.json()["error"])

# Form for inserting new records
st.header("Insert New Doctor Schedule")

with st.form("insert_form"):
    doctor_name = st.text_input("Doctor Name")
    monday = st.text_input("Monday Schedule")
    tuesday = st.text_input("Tuesday Schedule")
    wednesday = st.text_input("Wednesday Schedule")
    thursday = st.text_input("Thursday Schedule")
    friday = st.text_input("Friday Schedule")
    saturday = st.text_input("Saturday Schedule")
    sunday = st.text_input("Sunday Schedule")

    submit_button = st.form_submit_button("Insert Record")

    if submit_button:
        if not doctor_name:
            st.error("Doctor name is required!")
        else:
            data = {
                "doctor_name": doctor_name,
                "monday": monday,
                "tuesday": tuesday,
                "wednesday": wednesday,
                "thursday": thursday,
                "friday": friday,
                "saturday": saturday,
                "sunday": sunday
            }
            response = requests.post("http://localhost:5000/insert", json=data)
            if response.status_code == 200:
                st.success("Record inserted and vector database updated successfully!")
            else:
                st.error(f"Error: {response.json()['error']}")