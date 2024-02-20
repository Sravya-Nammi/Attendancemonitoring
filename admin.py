import streamlit as st
pip install streamlit-gsheets
title = st.text_input('Name', ' ')

attendance_marked = False

if st.button("Mark Attendance", type="primary"):
    # Implement logic to mark attendance (e.g., write data to the sheet)
    attendance_marked = True
    st.write("Attendance registered")

if st.button('Click Attendance'):
    if attendance_marked:
        st.write("Attendance already registered")
    else:
        st.write("Please click 'Mark Attendance' to register")

# Connect to Google Sheet (assuming you need it)
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# Example: Read specific data from the sheet
if attendance_marked:
    df = conn.read(
        worksheet="Sheet1",
        usecols=[0, 1],  # Read columns 0 and 1
        nrows=1,  # Read only the first row
    )
    for row in df.itertuples():
        st.write(f"{row.name} has a :{row.pet}:")




