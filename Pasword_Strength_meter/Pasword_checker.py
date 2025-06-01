import streamlit as st
import re  # For pattern matching

def check_password(password):
    """Check password strength and return score (1-5) and feedback"""
    score = 0
    feedback = []
    
    # 1. Length check (8+ characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password too short (needs 8+ characters)")
    
    # 2. Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z)")
    
    # 3. Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z)")
    
    # 4. Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers (0-9)")
    
    # 5. Special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add special chars (!@#$%^&*)")
    
    return score, feedback

# Simple Streamlit UI
st.title("🔐 Password Checker")
password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password(password)
    
    # Show strength
    if score <= 2:
        st.error(f"Weak (Score: {score}/5)")
    elif score <= 4:
        st.warning(f"Moderate (Score: {score}/5)")
    else:
        st.success(f"Strong (Score: {score}/5)")
    
    # Show improvement tips
    if feedback:
        st.write("To improve your password:")
        for tip in feedback:
            st.write(f"- {tip}")

st.write("Try a password that has:")
st.write("- At least 8 characters")
st.write("- Uppercase and lowercase letters")
st.write("- Numbers and special symbols")