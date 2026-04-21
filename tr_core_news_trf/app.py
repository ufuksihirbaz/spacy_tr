"""
Primary Purpose:
    This file serves as the Streamlit web interface for the custom Turkish spaCy model (tr_core_news_trf).

Core Logic/Components:
    - Imports `spacy_streamlit` for creating an interactive NLP visualization dashboard.
    - Configures the dashboard to load the locally assembled model located at `models/tr_core_news_trf-3.4.2`.
    - Provides a default Turkish text sample to demonstrate Named Entity Recognition (NER), POS tagging, and Dependency Parsing.
    - Invokes the `visualize()` function to render the UI.

Broader Application:
    This application allows developers and end-users to interactively test, visualize, and validate the capabilities 
    of the `tr_core_news_trf` model directly in a web browser, abstracting away the need for script-based inference.
"""

import streamlit as st
import spacy_streamlit

# Monkey-patch for spacy-streamlit compatibility with newer versions of Streamlit
if not hasattr(st, "experimental_rerun") and hasattr(st, "rerun"):
    st.experimental_rerun = st.rerun

def render_ui():
    """
    Main function to configure and render the Streamlit UI for the spaCy model.
    """
    # The path to the local assembled and packaged model
    models = ["models/tr_core_news_trf-3.4.2"]
    
    # A default Turkish text snippet to test NER, dependencies, and POS tagging out of the box
    default_text = (
        "Türkiye'nin başkenti Ankara'dır ve Türkiye Cumhuriyeti, 29 Ekim 1923'te "
        "Mustafa Kemal Atatürk tarafından kurulmuştur. İstanbul ise ülkenin en kalabalık şehridir."
    )
    
    # Generate the interactive UI using spacy-streamlit
    spacy_streamlit.visualize(
        models=models, 
        default_text=default_text,
        visualizers=["ner", "parser", "textcat", "similarity", "tokens"]
    )

if __name__ == "__main__":
    render_ui()
