import streamlit as st
import requests

# Hugging Face API details
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/mistral-7b-v0.1"
headers = {"Authorization": f"Bearer {st.secrets['HF_API_TOKEN']}"}

# Function to query the Hugging Face API
def query_hf_api(prompt):
    payload = {"inputs": prompt}
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error {response.status_code}: {response.text}"

# Streamlit UI
st.title("Simple Question Answering System")
st.write("Ask anything you want, and the Mistral model will generate a response!")

# Input for question
user_input = st.text_input("Your Question")

if st.button("Get Answer"):
    if user_input.strip():
        with st.spinner("Fetching response..."):
            response = query_hf_api(user_input)
        st.success("Answer:")
        st.write(response)
    else:
        st.warning("Please enter a valid question.")
