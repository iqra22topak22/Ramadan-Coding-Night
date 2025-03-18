import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")
def generate_money():
    return random.randint(1,1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)
    amount = generate_money()
    st.success(f"you made ${amount}!")

def fetch_side_hustle():
        try:
            response = requests.get('http://127.0.0.1:8000/side_hustles')
            if response.status_code ==200:
                hustles = response.json()
                return hustles["side_hustle"]
            else:
                return("freelancing")
        except:
            return("something went wrong")
        
st.subheader("side hustle Ideas")
if st.button("Generate hustle"):
    idea = fetch_side_hustle()
    st.success(idea)
# -------------------------------------------
def fetch_money_quote():
     try:
          response = requests.get('http://127.0.0.1:8000/money_quotes')
          if response.status_code == 200:
               quotes = response.json()
               return quotes["money_quote"]
          else:
               return("money is the root of all evil")
     except:
          return("something went wrong!")
     
st.subheader("Money-making Motivation")
if st.button("Get Inspired"):
     quote = fetch_money_quote()
     st.info(quote)