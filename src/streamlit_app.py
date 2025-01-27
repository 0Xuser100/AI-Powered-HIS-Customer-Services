import streamlit as st
import requests

st.title("Pain & Go Hospital Query System")

# Input for user query
query = st.text_input("Enter your query:")

# Button to submit query
if st.button("Submit"):
    response = requests.post("http://localhost:5000/query", json={"query": query})
    if response.status_code == 200:
        st.write("Response:", response.json()["answer"])
    else:
        st.write("Error:", response.json()["error"])