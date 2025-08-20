import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import sqlite3 
import google.generativeai as genai

st.set_page_config(page_title="API integration", layout="centered")
st.title("Gen AI Integration with Streamlit")


def home():
    st.title("Home")
    st.write("Welcome to the Home page!")

def sign_in():
    st.title("Sign IN")
    st.write("Please enter your credentials to sign in.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        try:
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = cur.fetchone()
            conn.close()
            if user:
                conn = sqlite3.connect('users.db')
                cur = conn.cursor()
                cur.execute("SELECT * FROM users")
                all_users = cur.fetchall()
                conn.close()
                st.write("All Users:")
                st.write(pd.DataFrame(all_users, columns=['Username', 'Password', 'Age', 'Email']))
                st.success("Signed in successfully!")
            else:
                st.error("Invalid username or password.")
        except sqlite3.Error as e:
            st.error(f"An error occurred: {e}")

def sign_up():
    st.title("Sign UP")
    st.write("Create a new account.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    email = st.text_input("Email")
    if st.button("Sign Up"):
        if username and password and email:
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, age INTEGER, email TEXT)")
            cur.execute("INSERT INTO users (username, password, age, email) VALUES (?, ?, ?, ?)", 
                        (username, password, age, email))
            conn.commit()
            conn.close()
            st.success("Account created successfully!")
        else:
            st.error("Please fill in all fields.")

def contact_us():
    st.title("Contact Us")
    st.write("Get in touch with us.")

def chat_with_ai():
    st.title("Chat with AI")
    prompt = st.text_input("Ask me anything:")
    if prompt and st.button("Send"):
        genai.configure(api_key="AIzaSyCAJ6CGik6Eg_wWJmSzALAcOx4rE7yCoW4")
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(contents=prompt)
        st.write(response.text)
        
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Sign IN', "Sign UP", "Contact Us", "Chat"], 
        icons=['house', 'box-arrow-in-right', 'person-add', 'envelope', 'chat'], menu_icon="cast", default_index=1)
    selected
    
if selected == "Home":
    home()
elif selected == "Sign IN":
    sign_in()
elif selected == "Sign UP":
    sign_up()
elif selected == "Contact Us":
    contact_us()
elif selected == "Chat":
    chat_with_ai()
    
    
        