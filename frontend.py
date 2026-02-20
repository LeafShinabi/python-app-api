import streamlit as st
import requests  # This is the 'bridge' library

st.set_page_config(page_title="Two-File App")
st.title("Python Frontend")

name = st.text_input("What is your name?")

if st.button("Send to Backend"):
    # 1. Reach out to the backend file via its local URL
    backend_url = f"http://127.0.0.1:5000/api/data?name={name}"
    
    try:
        # 2. GET the data from the other file
        response = requests.get(f"https://python-app-api.onrender.com/greet?name={user_name}")
        result = response.json()
        
        # 3. Display the result in the UI
        st.write("### Response from backend.py:")
        st.success(result['message'])
        st.info(f"The backend calculated your name length as: {result['data_length']}")
        
    except requests.exceptions.ConnectionError:
        st.error("Error: Is backend.py running?")