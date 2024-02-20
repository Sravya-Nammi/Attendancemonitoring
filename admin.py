import streamlit as st

title = st.text_input('Name', ' ')

st.button("Mark Attendance", type="primary")
if st.button('Click Attendance'):
    st.write('Attendance registered')
else:
    st.write('Not registered')
