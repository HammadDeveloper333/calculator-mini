import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the two numbers
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

# Operation selection
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the selected operation
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
        st.error("Cannot divide by zero")

# Display the result

    st.write(f"The result is: {result}")