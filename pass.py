import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")
st.markdown("""
## **Welcome to the Password Strength Checker!** 🔑  
Check how strong your password is and get **useful suggestions** to make it safer...✅🔒  
We will provide you with helpful tips to create a **strong password!** 🛡️✨
""")

password = st.text_input("Enter a password:", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should have at least 8 characters.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one uppercase and one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")
    
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")
    
    # Strength Bar
    st.markdown("### Password Strength⚡:")
    st.progress(score / 4)  # Normalizing the score to a scale of 0 to 1
    
    if score == 4:
        feedback.append("✅ Your password is strong! 👍🎉")
    elif score == 3:
        feedback.append("✔️ Password is moderately strong! 🟡.. But could be stronger.")
    else:
        feedback.append("❗ **Password is weak!** 🔴 .. But you can strengthen it.")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.markdown(tip)
else:
    st.info("Please enter a password.")
