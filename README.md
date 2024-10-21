import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")

# Function to perform calculations
def calculate(operation, num1, num2=None):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    elif operation == "Exponentiation":
        return num1 ** num2
    elif operation == "Square Root":
        return math.sqrt(num1)
    elif operation == "Sine":
        return math.sin(math.radians(num1))
    elif operation == "Cosine":
        return math.cos(math.radians(num1))
    elif operation == "Tangent":
        return math.tan(math.radians(num1))

# Select operation
operation = st.selectbox("Select operation:", [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Exponentiation",
    "Square Root",
    "Sine",
    "Cosine",
    "Tangent"
])

# Input numbers
num1 = st.number_input("Enter first number:", value=0.0)
num2 = None

if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]:
    num2 = st.number_input("Enter second number:", value=0.0)

# Calculate and display result
if st.button("Calculate"):
    if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]:
        result = calculate(operation, num1, num2)
    else:
        result = calculate(operation, num1)
    
    st.write(f"Result: {result}")
