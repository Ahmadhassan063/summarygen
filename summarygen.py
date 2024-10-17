import streamlit as st
from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization")

# Streamlit app title
st.title("Text Summary Generator")

# Text input area for the user
input_text = st.text_area("Enter text to summarize:", height=300)

# Button to generate the summary
if st.button("Generate Summary"):
    if input_text:
        # Generate summary
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
