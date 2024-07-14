import streamlit as st
from transformers import pipeline

# Streamlit App Title
st.title('Text Summarizer App')

# User Input for the text
st.write('Enter the text you want to summarize below:')
text_input = st.text_area('Text', '')

# Summarize Button
if st.button('Summarize'):
    if text_input:
        try:
            summarizer = pipeline("summarization")
            summary = summarizer(text_input, max_length=150, min_length=30, do_sample=False)
            summary_text = summary[0]['summary_text']
            if summary_text:
                st.subheader('Summary:')
                st.write(summary_text)
            else:
                st.write('Text is too short to summarize.')
        except Exception as e:
            st.write(f'An error occurred: {e}')
    else:
        st.write('Please enter some text to summarize.')
