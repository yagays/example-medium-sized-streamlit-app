import streamlit as st

st_sidebar = st.sidebar


def some_text():
    st_sidebar.write("This is sidebar text")


def select_animal():
    return st_sidebar.radio("What's your favorite animal?", ("Dog", "Cat"))
