import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="MBBC AI Doctor - Mental Health", page_icon="🧠", layout="centered")

st.title("🧠 MBBC AI Doctor - Mental Health")
st.subheader("মানসিক স্বাস্থ্যের জন্য সাজেশন")
st.caption("MBBC & Company Research Project | Data anonymous & used only for research")

if not st.checkbox("আমি সম্মতি দিচ্ছি যে আমার তথ্য গোপনীয়ভাবে MBBC গবেষণায় ব্যবহার হবে এবং এটা চিকিৎসা পরামর্শ নয়। (I consent)", key="consent_ment"):
    st.stop()

st.write("---")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("বয়স / Age", min_value=1, max_value=120, value=25)
    gender = st.selectbox("লিঙ্গ / Gender", ["পুরুষ / Male", "মহিলা / Female", "অন্যান্য / Other"])
with col2:
    district = st.text_input("জেলা / District", value="Dhaka")

st.write("**গত ২ সপ্তাহে কতবার এগুলো অনুভব করেছেন? (0 = কখনো না, 3 = প্রায় প্রতিদিন)**")
q1 = st.slider("১. কাজে মন বসে না / Little interest in doing things", 0, 3, 0)
q2 = st.slider("২. অস্থির বা চিন্তিত লাগে / Feeling down or anxious", 0, 3, 0)
q3 = st.slider("৩. ঘুমের সমস্যা / Trouble sleeping", 0, 3, 0)
extra = st.text_area("অন্য কোনো মানসিক সমস্যা বা চিন্তা বলুন (যেমন: উদ্বেগ, একা লাগা, আত্মহত্যার চিন্তা ইত্যাদি)", height=100)

if st.button("✅ Submit & Get Recommendation", type="primary"):
    score = q1 + q2 + q3
    summary = f"""
**Symptom Summary**  
- Age: {age} | Gender: {gender} | District: {district}  
- Score (0-9): {score}/9  
- Extra note: {extra}
    """
    st.success("✅ Your Symptom Summary")
    st.markdown(summary)

    if score >= 6:
        rec = "**Recommendation**: মাঝারি-উচ্চ মানসিক চাপ দেখা যাচ্ছে।\n\n**যেখানে যাবেন**: নিকটস্থ Upazila/District Hospital-এ Psychologist বা Psychiatrist দেখান।\n\n**জরুরি হেল্পলাইন**: Kaan Pete Roi (২৪ ঘণ্টা)\n- Grameenphone: 01779-554391 / 01779-554392\n- Airtel: 01688-709965\n\n**অন্যান্য**: 16767 (সরকারি মানসিক স্বাস্থ্য হেল্পলাইন)"
    elif score >= 3:
        rec = "**Recommendation**: হালকা চাপ/উদ্বেগ।\n\n**যেখানে যাবেন**: Community Clinic বা যেকোনো MBBS ডাক্তার দেখান। নিয়মিত ব্যায়াম ও ঘুমের রুটিন মেনে চলুন।\n\n**সাহায্য লাগলে**: Kaan Pete Roi হেল্পলাইন কল করুন।"
    else:
        rec = "**Recommendation**: ভালো অবস্থায় আছেন। সুস্থ থাকার জন্য নিয়মিত হাঁটাহাঁটি করুন।"

    st.markdown("### 🧠 Your Recommendation")
    st.markdown(rec)
    st.warning("⚠️ **This is NOT medical advice.** অবশ্যই BMDC রেজিস্টার্ড ডাক্তার বা মনোরোগ বিশেষজ্ঞের সাথে দেখা করুন।")

    data = {"Timestamp": datetime.now(), "Age": age, "Gender": gender, "District": district,
            "Score": score, "Extra": extra, "Page": "Mental Health"}
    df = pd.DataFrame([data])
    st.download_button("📥 Download your response", df.to_csv(index=False).encode('utf-8'), 
                       f"mbbc_mental_{datetime.now().strftime('%Y%m%d_%H%M')}.csv", "text/csv")
