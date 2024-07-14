import streamlit as st
import sumy
import gensim
import scipy

st.write(f"sumy version: {sumy.__version__}")
st.write(f"gensim version: {gensim.__version__}")
st.write(f"scipy version: {scipy.__version__}")

# Your existing imports and code
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Streamlit App Title
st.title('Text Summarizer App')

# User Input for the text
st.write('Enter the text you want to summarize below:')
text_input = st.text_area('Text', '')

# Summarize Button
if st.button('Summarize'):
    if text_input:
        try:
            parser = PlaintextParser.from_string(text_input, Tokenizer('english'))
            summarizer = TextRankSummarizer()
            summary = summarizer(parser.document, 2)  # Number of sentences in summary
            summary_text = ' '.join([str(sentence) for sentence in summary])
            if summary_text:
                st.subheader('Summary:')
                st.write(summary_text)
            else:
                st.write('Text is too short to summarize.')
        except Exception as e:
            st.write(f'An error occurred: {e}')
    else:
        st.write('Please enter some text to summarize.')
