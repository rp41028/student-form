import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")  # Make sure this file is in the same folder
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- Web Form ---
st.title("Student Registration Form")

name = st.text_input("Name")
roll = st.text_input("Roll Number")
course = st.text_input("Course")

if st.button("Submit"):
    if name and roll and course:
        student_data = {
            "name": name.strip(),
            "roll": roll.strip(),
            "course": course.strip()
        }
        db.collection("students").add(student_data)
        st.success(f"Student {name} added successfully!")
    else:
        st.error("All fields are required.")
