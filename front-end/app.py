import streamlit as st
import requests

st.set_page_config(page_title="Healthcare Report Generator", layout="centered")
st.title("Personalized Healthcare Report Generator 🩺🥼💉")

symptoms = st.text_area("Enter your symptoms:", placeholder="e.g., headache, fever, sore throat")

if st.button("Generate Report"):
    if not symptoms.strip():
        st.warning("Please enter some symptoms.")
    else:
        with st.spinner("Generating your report..."):
            response = requests.post("http://localhost:8000/generate-report", json={"symptoms": symptoms})
            if response.status_code == 200:
                st.subheader("Your Personalized Healthcare Report")
                st.code(response.json()["report"], language="markdown")
            else:
                st.error("Something went wrong. Please try again.")