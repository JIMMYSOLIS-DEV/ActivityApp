import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Database credentials
DATABASE_URL = 'mysql+mysqlconnector://root:@localhost/demo'

# Set page config
st.set_page_config(page_title="User Manager", layout="centered")

# Connect to database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Title
st.title("🧑‍💼 User Management Dashboard")

# Show all users
st.header("📋 User Table")
df = pd.read_sql("SELECT * FROM users", engine)
st.dataframe(df, use_container_width=True)

# Columns for forms
col1, col2 = st.columns(2)

# Insert new user
with col1:
    st.subheader("➕ Add User")
    with st.form(key='insert_form'):
        name = st.text_input("Name")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Add User")
        if submit:
            with engine.connect() as conn:
                conn.execute(text("INSERT INTO users (name, password) VALUES (:name, :password)"),
                             {"name": name, "password": password})
                conn.commit()
            st.success("✅ User added!")

# Login form
with col2:
    st.subheader("🔐 User Login")
    with st.form(key='login_form'):
        username = st.text_input("Username")
        user_password = st.text_input("Password", type="password")
        login = st.form_submit_button("Login")
        if login:
            query = text("SELECT * FROM users WHERE name = :username AND password = :password")
            result = pd.read_sql(query, engine, params={"username": username, "password": user_password})
            if not result.empty:
                st.success(f"🎉 Welcome, {username}!")
            else:
                st.error("❌ Invalid credentials")
