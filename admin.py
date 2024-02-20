import streamlit as st

title = st.text_input('Name', ' ')

st.button("Mark Attendance", type="primary")
if st.button('Click Attendance'):
    st.write('Attendance registered')
else:
    st.write('Not registered')
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/1UovzMG1X88aHLXsU9k61QLR1if5BFB2LGHSCYXBxwjw/edit?usp=sharing"

from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)
# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")



