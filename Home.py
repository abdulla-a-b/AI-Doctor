import streamlit as st

st.set_page_config(page_title="MBBC AI Doctor", page_icon="🩺", layout="wide")

st.title("👋 Welcome to MBBC AI Doctor")
st.subheader("MBBC & Company Research Project")
st.write("**AI Doctor for Bangladesh** – Share your physical or mental symptoms and get recommendation where to go for treatment.")

st.markdown("### Choose your category:")
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_🩺_General_Health.py", label="🩺 General Health (শারীরিক সমস্যা)", icon="🩺", use_container_width=True)

with col2:
    st.page_link("pages/2_🧠_Mental_Health.py", label="🧠 Mental Health (মানসিক সমস্যা)", icon="🧠", use_container_width=True)

st.info("After submitting symptoms you will see summary + doctor/hospital recommendation.\nAll data is anonymous and used only for our 2000-patient research.")
st.caption("© MBBC & Company | Developed for Smart Bangladesh 2041")
