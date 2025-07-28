import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    # Load data from file
    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.load(fs)
    except Exception as err:
        print(f"Error loading data: {err}")

    @classmethod
    def _update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def _generate_account(cls):
        id = random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=7)
        random.shuffle(id)
        return ''.join(id)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return None, "You must be at least 18 and use a 4-digit PIN."
        acc_no = cls._generate_account()
        user = {
            "name": name,
            "age": age,
            "e-mail": email,
            "pin": pin,
            "accountNo": acc_no,
            "balance": 0
        }
        cls.data.append(user)
        cls._update()
        return acc_no, "Account created successfully!"

    @classmethod
    def get_user(cls, acc_no, pin):
        return next((u for u in cls.data if u["accountNo"] == acc_no and u["pin"] == pin), None)

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        user = cls.get_user(acc_no, pin)
        if not user:
            return "Invalid account or PIN."
        if amount <= 0 or amount > 10000:
            return "Deposit must be between ₹1 and ₹10,000."
        user["balance"] += amount
        cls._update()
        return "Deposit successful."

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        user = cls.get_user(acc_no, pin)
        if not user:
            return "Invalid account or PIN."
        if user["balance"] < amount:
            return "Insufficient balance."
        user["balance"] -= amount
        cls._update()
        return "Withdrawal successful."

    @classmethod
    def update(cls, acc_no, pin, name=None, email=None, new_pin=None):
        user = cls.get_user(acc_no, pin)
        if not user:
            return "Invalid account or PIN."
        if name:
            user["name"] = name
        if email:
            user["e-mail"] = email
        if new_pin and len(str(new_pin)) == 4:
            user["pin"] = new_pin
        cls._update()
        return "Details updated successfully."

    @classmethod
    def delete(cls, acc_no, pin):
        user = cls.get_user(acc_no, pin)
        if not user:
            return "Invalid account or PIN."
        cls.data.remove(user)
        cls._update()
        return "Account deleted successfully."

