
import streamlit as st
import random
import string

# Password generate karne ka function
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Small aur capital letters ke liye
    if use_digits:
        characters += string.digits   # Numbers 0-9 ko add karna
    if use_special:
        characters += string.punctuation # Special characters jese @#$% ko add karna
    return "".join(random.choice(characters) for _ in range(length))  # Randomly characters select karna

# Streamlit ka interface
st.title("Password Generator")

# Password ki length ko select karne ke liye slider
length = st.slider("Password ki length choose karein", min_value=6, max_value=32, value=12)

# Checkboxes jo decide karenge ke digits aur special characters include karne hain ya nahi
use_digits = st.checkbox("Digits shamil karein")
use_special = st.checkbox("Special characters shamil karein")

# Password generate karne ka button
if st.button("Password Generate karein"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")  # Generate kiya gaya password dikhana

# Footer
st.write("-----------------------------")
st.write("Build with ❤️ by [Iqra Mushtaq](https://github.com/IqraMushtaq)")

