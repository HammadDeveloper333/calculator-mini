import streamlit as st

st.title("Simple Calculator")

# Get user input for the numbers
num1 = st.number_input("Enter the first number", format="%f")
num2 = st.number_input("Enter the second number", format="%f")

# Get user input for the operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
st.write(f"The result is: {result}")
