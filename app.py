from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PriceFit",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default padding/header so the page fills the window.
st.markdown(
    """
    <style>
      #MainMenu, footer, header {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "pricefit.html").read_text(encoding="utf-8")

# The whole app runs in the browser (plain JavaScript), so Streamlit just serves it.
components.html(html, height=1400, scrolling=True)
