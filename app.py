import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Streamlit Demo App", page_icon="🎉")
st.title('Welcome to the Streamlit Demo App 🎉')

# Add some custom CSS to improve the design
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stNumberInput>div>div>input {
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stHeader {
        color: #FF6347;
        font-family: 'Arial', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Header and User Input
st.header('Enter Your Details Below')

# Create input fields for user information
user_name = st.text_input("Enter your name:", max_chars=50)
age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)

# Button to submit the details
if st.button('Submit'):
    if user_name and age:
        st.success(f"Hello {user_name}, you are {age} years old!")
    else:
        st.error("Please provide both name and age.")
