# 🔐 MySQL Username Lookup Script

This Python script allows you to securely connect to a MySQL database and search for a user by their username.

## 📋 Features

- Connects to a MySQL database using `mysql-connector-python`
- Prompts the user for a username and searches for it in the `users` table
- Uses parameterized queries to prevent SQL injection
- Clean and readable structure with proper error handling
- Fully documented with English comments

## 🛠 Requirements

- Python 3.x
- `mysql-connector-python` library
- A MySQL server running locally with a database named `test` and a table called `users`

## ⚙️ Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install mysql-connector-python
```

## 🔧 Configuration

Make sure to update the database connection settings in the script if needed:

```python
host='localhost',
user='root',
password='your-password',
database='test'
```

## 🚀 Usage

Run the script with:

```bash
python find_user.py
```

Then enter a username to search in your `users` table.

## 🐧 Linux Compatible

✅ This script works perfectly on Linux systems.

## 📁 File Structure

```
.
├── find_user.py         # Main script
└── README.md            # This file
```

## 🧠 Author

Made with ❤️ by Erfan ([@Erphs](https://github.com/Erphs))

## 📄 License

Feel free to use and modify this script for learning or development purposes.