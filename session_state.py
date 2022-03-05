import streamlit as st


def initialize():
    if "counter" not in st.session_state:
        st.session_state["counter"] = 0
