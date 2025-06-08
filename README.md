# Password Generator Automation 🔐

This project automates the testing of a password generator website using Selenium and Pytest.

🛠 Tech Stack

![Python](https://img.shields.io/badge/python-3.11-blue.svg?logo=python)
![Selenium](https://img.shields.io/badge/selenium-4.20.0-brightgreen.svg?logo=selenium)
![PyTest](https://img.shields.io/badge/pytest-8.1.1-yellow.svg?logo=pytest)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=github)
![HTML Report](https://img.shields.io/badge/report-html-orange)


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
