# Password Generator Automation 🔐

This project automates the testing of a password generator website using Selenium and Pytest.

## ✔ Features Tested

- Password format selection (e.g., lowercase, mixed case)
- Password length verification
- UI element interaction with Selenium

## 📁 Project Structure

password-generator-automation/
├── tests/
│ └── test_generate_password.py
├── requirements.txt
├── .gitignore
└── README.md



## ▶ How to Run

1. Create virtual environment:

python -m venv venv
venv\Scripts\activate  # on Windows
Install dependencies:


pip install -r requirements.txt
Run tests:


pytest tests/ --html=report.html


🛠 Tech Stack

Python

Selenium

Pytest
