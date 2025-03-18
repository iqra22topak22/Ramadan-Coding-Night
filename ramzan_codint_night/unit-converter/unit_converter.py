import streamlit as st
import pandas as pd

def convert_units(value , unit_form, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter":1000,
        "gram_kilogram":0.001,
        "kilogram_gram":1000

    }
    key = f"{unit_form}_{unit_to}"
    if key in conversions:
        conversions = conversions[key]
        return value * conversions
   
    else:
        return "conversions not supported"

st.title("Unit Converter")

value = st.number_input("Enter the value to convert:")

unit_from =st.selectbox("convert from :",["meter", "kilometer","gram","kilogram"])

unit_to = st.selectbox("convert to:",["meter","kilometer","gram","kilogram"])

if st.button("convert"):
    result = convert_units(value, unit_from,unit_to)
    st.write(f"converted value: {result}")