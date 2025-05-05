import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="CSV File Uploader", page_icon="📊")
st.title('📈 CSV File Uploader and Filter')

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# If file is uploaded
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Display raw data if checkbox is checked
    if st.checkbox('Show raw data'):
        st.write(df)
    
    st.subheader('Data Preview:')
    st.dataframe(df)

    # Column filter (only if there are enough columns)
    if len(df.columns) >= 5:
        column = st.selectbox("Select column to filter by:", df.columns)
        selected_value = st.selectbox(f"Select a value from {column}:", df[column].unique())
        filtered_df = df[df[column] == selected_value]
        st.write(f"Filtered data by {column} = {selected_value}")
        st.dataframe(filtered_df)
else:
    st.write("Please upload a CSV file to begin.")
