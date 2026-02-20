import streamlit as st
import requests

st.set_page_config(page_title="Two-File App")
st.title("Python Frontend")

# You named it 'name' here
name = st.text_input("What is your name?")

if st.button("Send to Backend"):
    try:
        # Changed 'user_name' to 'name' to match the variable above
        response = requests.get(f"https://python-app-api.onrender.com/greet?name={name}")
        result = response.json()
        
        st.write("### Response from backend.py:")
        st.success(result['message'])
        
        # Note: Make sure your backend API actually returns 'data_length'
        # if it doesn't, this line will cause a 'KeyError'
        if 'data_length' in result:
            st.info(f"The backend calculated your name length as: {result['data_length']}")
        
    except requests.exceptions.ConnectionError:
        st.error("Error: Could not connect to the backend URL.")