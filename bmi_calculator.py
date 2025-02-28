import streamlit as st

st.title(" Multi-Purpose Calculator")

menu = st.sidebar.radio("Select a Calculator", ["BMI Calculator", "Simple Calculator"])

if menu == "BMI Calculator":
    st.header("📊 BMI Calculator")

    weight = st.number_input("Enter your weight (kg):", min_value=1.0, max_value=200.0, value=70.0, step=0.1)
    height = st.number_input("Enter your height (m):", min_value=0.5, max_value=2.5, value=1.70, step=0.01)

    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"### 📊 Your BMI: **{bmi:.2f}**")
    else:
        st.write("⚠️ Please enter a valid height.")

    if bmi < 18.5:
        st.write("🔵 **Underweight**")
    elif 18.5 <= bmi < 24.9:
        st.write("🟢 **Normal Weight**")
    elif 25.0 <= bmi < 29.9:
        st.write("🟠 **Overweight**")
    else:
        st.write("🔴 **Obese**")

elif menu == "Simple Calculator":
    st.header("🧮 Simple Calculator")

    num1 = st.number_input("Enter first number:", value=0.0, step=0.1)
    num2 = st.number_input("Enter second number:", value=0.0, step=0.1)

    operation = st.selectbox("Select an operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

    result = None
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (*)":
        result = num1 * num2
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "⚠️ Cannot divide by zero!"

    
    st.write("### 🔢 Result:")
    st.write(f"**{result}**")
