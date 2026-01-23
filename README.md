# Cryptography-Methods 🔐 || Classical Cipher Playground

A clean and educational Python cryptography project that implements classical encryption and decryption techniques.
The project is designed to clearly separate backend cryptographic logic from a simple frontend interface, making it ideal for learning how ciphers work and how backend–frontend communication is structured.

PRESS THE GIF TO SEE THE PROJECT  ⬇️

[![My Website](https://github.com/user-attachments/assets/e7e0d6be-bcbf-4968-be98-ac32af4a2dac)](https://cryptography-methods.netlify.app/)

# Features

🔐 Implementation of classical cryptographic algorithms

📊 English text detection using frequency analysis

🌐 Frontend interface built with HTML, CSS, and JavaScript

⚙️ Backend logic written in Python

# Project Structure
```text
cryptography-methods/
│
├── Backend/                         # Cryptographic logic (Python)
│   │
│   ├── main.py                      # Backend entry point
│   ├── english_detector.py          # English text detection logic
│   ├── english_dictionary.txt       # Dictionary used for validation
│   │
│   ├── Cesar/                       # Caesar cipher implementation
│   │   ├── cesar_cipher.py          # Encrypt / decrypt logic
│   │   └── cesar_hack.py            # Brute-force attack
│   │
│   ├── Simple_Column_Transposition/ # Columnar transposition cipher
│   │   └── simple_column_transposition_cipher.py
│
├── Frontend/                        # User interface
│   │
│   ├── index.html                   # Main HTML page
│   ├── style.css                    # Styling
│   └── script.js                    # Frontend logic
│
├── requirements.txt                 # Python dependencies
├── LICENSE                          # License information
└── README.md                        # Project documentation

```

# Build & Run

Requirements: Python 3.x

# Backend setup:

```bash
git clone https://github.com/your-username/cryptography-methods.git
cd cryptography-methods
pip install -r requirements.txt
python Backend/main.py
```
# Frontend:

Open : Index.html

# Purpose of the Project 🎯

This project was created as a learning-focused cryptography playground to practice:

-Understanding classical encryption methods

-Applying brute-force and frequency analysis techniques

-Structuring a backend–frontend project

-Working with real text validation (English detection)

**It is especially useful for:**

-Students learning cryptography basics

-Beginners practicing Python backend logic

