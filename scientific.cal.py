
import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")

# Function to perform calculations
def calculate(operation, num1, num2=None):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2 if num2 != 0 else "Error! Division by zero."
    elif operation == 'Power':
        return num1 ** num2
    elif operation == 'Square Root':
        return math.sqrt(num1)
    elif operation == 'Sine':
        return math.sin(math.radians(num1))
    elif operation == 'Cosine':
        return math.cos(math.radians(num1))
    elif operation == 'Tangent':
        return math.tan(math.radians(num1))
    elif operation == 'Logarithm':
        return math.log(num1, num2) if num2 > 0 else "Error! Logarithm of non-positive number."

# Dropdown for operation selection
operation = st.selectbox("Select operation", [
    'Add', 'Subtract', 'Multiply', 'Divide', 
    'Power', 'Square Root', 'Sine', 'Cosine', 
    'Tangent', 'Logarithm'
])

# Input fields for numbers
if operation in ['Add', 'Subtract', 'Multiply', 'Divide', 'Power']:
    num1 = st.number_input("Enter first number", format="%.6f")
    num2 = st.number_input("Enter second number", format="%.6f")
    result = calculate(operation, num1, num2)
elif operation in ['Square Root', 'Sine', 'Cosine', 'Tangent']:
    num1 = st.number_input("Enter number/angle", format="%.6f")
    result = calculate(operation, num1)
elif operation == 'Logarithm':
    num1 = st.number_input("Enter number", format="%.6f")
    num2 = st.number_input("Enter base", format="%.6f", value=10.0)
    result = calculate(operation, num1, num2)

# Display the result
if 'result' in locals():
    st.write(f"Result: {result}")
