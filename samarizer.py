import streamlit as st
from gensim.summarization import summarize

# Streamlit App Title
st.title('Text Summarizer App')

# User Input for the text
st.write('Enter the text you want to summarize below:')
text_input = st.text_area('Text', '')

# Summarize Button
if st.button('Summarize'):
    if text_input:
        try:
            summary = summarize(text_input)
            if summary:
                st.subheader('Summary:')
                st.write(summary)
            else:
                st.write('Text is too short to summarize.')
        except ValueError:
            st.write('Text is too short to summarize.')
    else:
        st.write('Please enter some text to summarize.')
