import streamlit as st

st.set_page_config(page_title="Sign Up", page_icon=":pencil:", layout="centered")
st.title("Sign Up Form")
st.write("Please fill in the details below to create an account.")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=80, value=18)
gender = st.radio("Gender", ("Male", "Female", "Other"))
skills = st.multiselect("Skills", ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"])
dob = st.date_input("Date of Birth", value=None, min_value=None, max_value=None, key=None)
exprience = st.slider("Years of Experience", 0, 30, 1)
submit_button = st.button("Sign Up")

if submit_button:
    if not name:
        st.error("Please enter your name.")
    elif age < 1 or age > 80:
        st.error("Please enter a valid age between 1 and 80")
    elif skills == []:
        st.error("Please select at least one skill.")
    elif not dob:
        st.error("Please select your date of birth.")
    elif exprience < 0 or exprience > 30:
        st.error("Please enter a valid years of experience between 0 and 30.")
    else:
        st.write("Thank you for signing up!")
        st.table([{"Name" : name, "Age" : age , "Gender" : gender, "Skills" : skills, "data of birth" : dob, "Experience" : exprience}])