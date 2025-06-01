import streamlit as st

st.title("📏 Unit Converter")

unit_type = st.selectbox(
    "Select Unit Type",
    ("Length", "Weight", "Temperature")
)

if unit_type == "Length":
    col1, col2 = st.columns(2)
    with col1:
        length_value = st.number_input("Enter value", min_value=0.0, key="length_val")
        from_unit = st.selectbox("From", ["Meters", "Feet", "Inches", "Kilometers", "Miles"], key="length_from")
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Feet", "Inches", "Kilometers", "Miles"], key="length_to")
    
    # Conversion factors to meters (base unit)
    to_meters = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Miles": 1609.34
    }
    
    if st.button("Convert", key="length_convert"):
        try:
            # Convert to meters first, then to target unit
            meters = length_value * to_meters[from_unit]
            converted_value = meters / to_meters[to_unit]
            st.success(f"**Result:** {length_value} {from_unit} = {converted_value:.6f} {to_unit}")
        except:
            st.error("Invalid conversion")

elif unit_type == "Weight":
    col1, col2 = st.columns(2)
    with col1:
        weight_value = st.number_input("Enter value", min_value=0.0, key="weight_val")
        from_unit = st.selectbox("From", ["Kilograms", "Pounds", "Grams", "Ounces", "Tons"], key="weight_from")
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Pounds", "Grams", "Ounces", "Tons"], key="weight_to")
    
    # Conversion factors to kilograms (base unit)
    to_kilograms = {
        "Kilograms": 1,
        "Pounds": 0.453592,
        "Grams": 0.001,
        "Ounces": 0.0283495,
        "Tons": 907.185
    }
    
    if st.button("Convert", key="weight_convert"):
        try:
            # Convert to kg first, then to target unit
            kg = weight_value * to_kilograms[from_unit]
            converted_value = kg / to_kilograms[to_unit]
            st.success(f"**Result:** {weight_value} {from_unit} = {converted_value:.6f} {to_unit}")
        except:
            st.error("Invalid conversion")

elif unit_type == "Temperature":
    col1, col2 = st.columns(2)
    with col1:
        temp_value = st.number_input("Enter temperature", key="temp_val")
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_from")
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_to")
    
    if st.button("Convert", key="temp_convert"):
        try:
            # First convert to Celsius (base unit)
            if from_unit == "Celsius":
                celsius = temp_value
            elif from_unit == "Fahrenheit":
                celsius = (temp_value - 32) * 5/9
            elif from_unit == "Kelvin":
                celsius = temp_value - 273.15
            
            # Then convert from Celsius to target unit
            if to_unit == "Celsius":
                converted_value = celsius
            elif to_unit == "Fahrenheit":
                converted_value = (celsius * 9/5) + 32
            elif to_unit == "Kelvin":
                converted_value = celsius + 273.15
            
            st.success(f"**Result:** {temp_value} {from_unit} = {converted_value:.2f} {to_unit}")
        except:
            st.error("Invalid conversion")