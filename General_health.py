import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="MBBC AI Doctor - General Health", page_icon="🩺", layout="centered")

st.title("🩺 MBBC AI Doctor - General Health")
st.subheader("শারীরিক সমস্যার জন্য সাজেশন")
st.caption("MBBC & Company Research Project | Data anonymous & used only for research")

if not st.checkbox("আমি সম্মতি দিচ্ছি যে আমার তথ্য গোপনীয়ভাবে MBBC গবেষণায় ব্যবহার হবে এবং এটা চিকিৎসা পরামর্শ নয়। (I consent)", key="consent_gen"):
    st.stop()

st.write("---")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("বয়স / Age", min_value=1, max_value=120, value=30)
    gender = st.selectbox("লিঙ্গ / Gender", ["পুরুষ / Male", "মহিলা / Female", "অন্যান্য / Other"])
with col2:
    district = st.text_input("জেলা / District (যেমন: Dhaka, Chattogram, Sylhet)", value="Dhaka")

symptom = st.text_area("আপনার প্রধান সমস্যা কী? (জ্বর, কাশি, পেট ব্যথা, মাথা ব্যথা ইত্যাদি লিখুন)", 
                       placeholder="উদাহরণ: ৩ দিন ধরে জ্বর ও শরীর ব্যথা", height=100)

details = st.text_area("আরও বিস্তারিত বলুন (কবে শুরু, কতদিন, কীতে বাড়ে/কমে, অন্য লক্ষণ আছে কি?)", height=150)

if st.button("✅ Submit & Get Recommendation", type="primary"):
    if not symptom.strip():
        st.error("Please describe your symptom")
    else:
        summary = f"""
**Symptom Summary**  
- Age: {age} | Gender: {gender} | District: {district}  
- Main Problem: {symptom}  
- Details: {details}
        """
        st.success("✅ Your Symptom Summary")
        st.markdown(summary)

        lower_sym = (symptom + " " + details).lower()
        if any(word in lower_sym for word in ["জ্বর", "fever", "কাশি", "cough", "শ্বাস", "breath"]):
            rec = "**Recommendation**: সাধারণ জ্বর/ফ্লু/সংক্রমণ হতে পারে।\n\n**যেখানে যাবেন**: নিকটস্থ Community Clinic বা Upazila Health Complex-এ General Physician দেখান।\n\n**অন্যান্য**: প্রচুর পানি খান, বিশ্রাম নিন। ২-৩ দিন না কমলে ডাক্তার দেখান।\n\n**জরুরি হলে**: ১৬২৬৩ হেল্পলাইন কল করুন।"
        elif any(word in lower_sym for word in ["পেট", "stomach", "ব্যথা", "pain", "ডায়রিয়া", "diarrhea"]):
            rec = "**Recommendation**: পেটের সমস্যা।\n\n**যেখানে যাবেন**: Community Clinic বা Upazila Health Complex-এ Medicine Doctor দেখান।\n\n**অন্যান্য**: ORS খান। রক্ত পায়খানা/বমি হলে তাড়াতাড়ি হাসপাতালে যান।"
        else:
            rec = "**Recommendation**: সাধারণ সমস্যা মনে হচ্ছে।\n\n**যেখানে যাবেন**: নিকটস্থ Community Clinic বা যেকোনো MBBS ডাক্তার দেখান।\n\n**খুঁজুন**: Google Maps-এ 'nearest community clinic near me' লিখুন।"

        st.markdown("### 🏥 Your Recommendation")
        st.markdown(rec)
        st.warning("⚠️ **This is NOT medical advice.** অবশ্যই BMDC রেজিস্টার্ড ডাক্তারের সাথে দেখা করুন।")

        data = {"Timestamp": datetime.now(), "Age": age, "Gender": gender, "District": district,
                "Symptom": symptom, "Details": details, "Page": "General Health"}
        df = pd.DataFrame([data])
        st.download_button("📥 Download your response (for your record)", df.to_csv(index=False).encode('utf-8'), 
                           f"mbbc_general_{datetime.now().strftime('%Y%m%d_%H%M')}.csv", "text/csv")
