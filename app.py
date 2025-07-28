import streamlit as st
from bank import Bank

st.set_page_config(page_title="💳 Simple Bank System", layout="centered")

st.title("🏦 Python Bank Management App")

menu = st.sidebar.radio("Select an option:", [
    "Create Account",
    "Deposit",
    "Withdraw",
    "Show Details",
    "Update Info",
    "Delete Account"
])

if menu == "Create Account":
    st.header("🔐 Open a New Account")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, step=1)
    email = st.text_input("Enter your email")
    pin = st.text_input("Set a 4-digit PIN", type="password")

    if st.button("Create Account"):
        if not (name and email and pin and age):
            st.warning("Please fill in all fields.")
        elif not (pin.isdigit() and len(pin) == 4):
            st.warning("PIN must be exactly 4 digits.")
        else:
            acc_no, msg = Bank.create_account(name, age, email, int(pin))
            if acc_no:
                st.success(msg)
                st.info(f"🆔 Your generated account number is: `{acc_no}`\n\n📌 Please note it down carefully!")
            else:
                st.error(msg)


if menu == "Deposit":
    st.header("💰 Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Deposit Amount", min_value=1, max_value=10000)

    if st.button("Deposit"):
        msg = Bank.deposit(acc, int(pin), int(amt))
        st.success(msg)

if menu == "Withdraw":
    st.header("💸 Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Withdrawal Amount", min_value=1)

    if st.button("Withdraw"):
        msg = Bank.withdraw(acc, int(pin), int(amt))
        st.success(msg)

if menu == "Show Details":
    st.header("📋 View Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        user = Bank.get_user(acc, int(pin))
        if user:
            st.json(user)
        else:
            st.error("Invalid account or PIN.")

if menu == "Update Info":
    st.header("✏️ Update Account Info")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New name (optional)")
    email = st.text_input("New email (optional)")
    new_pin = st.text_input("New 4-digit PIN (optional)")

    if st.button("Update"):
        msg = Bank.update(acc, int(pin), name=name, email=email, new_pin=int(new_pin) if new_pin else None)
        st.success(msg)

if menu == "Delete Account":
    st.header("⚠️ Delete Your Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        confirm = st.checkbox("Are you sure you want to delete your account?")
        if confirm:
            msg = Bank.delete(acc, int(pin))
            st.success(msg)
