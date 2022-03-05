import streamlit as st


def show_image(selected_animal):
    if selected_animal == "Dog":
        st.image("https://cdn.stocksnap.io/img-thumbs/960w/husky-animal_XC8FVWPQC3.jpg")
    elif selected_animal == "Cat":
        st.image("https://cdn.stocksnap.io/img-thumbs/960w/animal-face_2P4CSFCJYF.jpg")
    else:
        pass


def increment_counter_button():
    if st.button("+1"):
        st.session_state["counter"] += 1


def decrement_counter_button():
    if st.button("-1"):
        st.session_state["counter"] -= 1
