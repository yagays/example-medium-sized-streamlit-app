import streamlit as st

import ui.sidebar
import ui.main
import session_state

session_state.initialize()

ui.sidebar.some_text()
selected_animal = ui.sidebar.select_animal()

st.title("Sample App")

st.subheader("Select Button")
ui.main.show_image(selected_animal)

st.subheader("Session State and Counter")
col1, col2 = st.columns(2)
with col1:
    ui.main.increment_counter_button()
with col2:
    ui.main.decrement_counter_button()

st.write(f"Current counter: " + str(st.session_state["counter"]))
