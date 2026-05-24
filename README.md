# Python-ATM-With-Database
# 🏦 Python ATM System with JSON Database

This is a terminal-based ATM simulation project built with Python. The main feature of this project is that it uses a real JSON file as a database to save user information permanently.

---

## 🚀 Features

* **JSON Database Storage:** All users, card details, and balances are saved in `bank_database.json`. Even if you close the program, your data is not lost.
* **Randomized Card Creation:** Generates a random 8-digit IBAN, 3-digit CVV, and 5-digit Support Code for new users. *(Note: Currently it uses standard random generation. I am planning to add a loop to check database for %100 uniqueness in the next update).*
* **Banking Operations:** You can deposit, withdraw, and transfer money to other IBANs with real-time balance checks.
* **PIN Management:** Users can change their PIN. The system checks the database to make sure no two users have the same PIN.
* **Session Logs:** Tracks transaction history (deposits, withdrawals, support calls) during the active session.

---

## 🛠️ How It Works

* Uses `try-except` blocks to check if the database file exists at startup.
* Uses nested Python dictionaries to organize user data.
* Uses Python's built-in `json` module to read and write data.

---

## 💻 Tech Stack

* Python 3.x
* Built-in modules: `json`, `random`

---

### 👨‍💻 Developer
Developed by **Emir Özlük**.
