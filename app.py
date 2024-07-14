import streamlit as st
import nltk
from nltk.data import find
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Download the NLTK 'punkt' tokenizer if not already present
try:
    find('tokenizers/punkt')
except LookupError:
    st.write("Downloading NLTK 'punkt' tokenizer...")
    nltk.download('punkt')

# Streamlit App Title
st.title('Text Summarizer App')

# User Input for the text
st.write('Enter the text you want to summarize below:')
text_input = st.text_area('Text', '')

# Summarize Button
if st.button('Summarize'):
    if text_input:
        try:
            st.write("Starting summarization process...")
            parser = PlaintextParser.from_string(text_input, Tokenizer('english'))
            summarizer = TextRankSummarizer()
            summary = summarizer(parser.document, 2)  # Number of sentences in summary
            summary_text = ' '.join([str(sentence) for sentence in summary])
            st.write("Summarization process completed.")
            if summary_text:
                st.subheader('Summary:')
                st.write(summary_text)
            else:
                st.write('Text is too short to summarize.')
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.write("Please check the detailed logs in the Streamlit Cloud dashboard for more information.")
    else:
        st.write('Please enter some text to summarize.')
