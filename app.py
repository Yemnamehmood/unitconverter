import streamlit as st

# Custom Page Config
st.set_page_config(page_title="UniConvertX – The Ultimate Unit Transformer", page_icon="🔄", layout="centered")

# Custom CSS for amazing UI
st.markdown("""
    <style>
        body { background-color:white ; color:white; }
        .stApp { background: linear-gradient(to right, #0f2027, #203a43, #2c5364); }
        .title { font-size: 2.8em; font-weight: bold; text-align: center; color: #ffcc00; }
        .sub-title { text-align: center; color: #bbb; font-size: 1.3em; margin-bottom: 20px; }
        .footer { text-align: center; margin-top: 30px; font-size: 1.1em; color: #ffcc00; }
        .stSelectbox label, .stNumberInput label {
            color: #ffcc00 !important;
            font-weight: bold;
            font-size: 1.1em;
        .stSubheader {
            color: #ffcc00 !important;
            font-weight: bold;
            font-size: 1.4em;
        }
            /* Ensure dropdowns show an arrow cursor */
        div[data-baseweb="select"] * {
            cursor: pointer !important;
        }

        /* Fix cursor for subheaders & headings */
        .stSubheader, .stMarkdown p, .stMarkdown h2, .stMarkdown h3 {
            cursor: default !important;
        }




    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<p class="title">UniConvertX – The Ultimate Unit Transformer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Easily convert units and currencies with accuracy</p>', unsafe_allow_html=True)

# Unit Conversion Logic
unit_types = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
    "Temperature": {"Celsius": 1, "Fahrenheit": 1.8, "Kelvin": 1},
}

# Select Unit Type
unit_category = st.selectbox("Select Category ", list(unit_types.keys()))

# Select From & To Units
from_unit = st.selectbox("From", list(unit_types[unit_category].keys()))
to_unit = st.selectbox("To", list(unit_types[unit_category].keys()))

# Input Value
value = st.number_input(f"Enter value in {from_unit}", min_value=0.0, step=0.1)

# Convert Function
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        else:
            return value
    else:
        return value * (unit_types[category][to_unit] / unit_types[category][from_unit])

# Display Conversion Result
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_category)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")


# 📜 Footer
st.markdown('<p class="footer">✨ Made by Yemna Mehmood ✨</p>', unsafe_allow_html=True)
