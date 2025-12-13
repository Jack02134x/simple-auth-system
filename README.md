# Secure Authentication System

A simple yet secure user authentication system built using **Python**, **Flask**, **MariaDB (MySQL-compatible)**, and **HTML**. This project demonstrates core backend concepts such as password hashing, session-based authentication, database integration, and secure configuration management.

> ⚠️ This project is intentionally minimal and educational. The focus is on correctness, security basics, and clean structure rather than UI or advanced features.

---

## ✨ Features

* User registration and login
* Secure password hashing using **bcrypt**
* Session-based authentication
* Protected routes (authenticated users only)
* MariaDB/MySQL database integration
* Environment-variable based configuration

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **Database:** MariaDB (MySQL-compatible)
* **Security:** bcrypt
* **Frontend:** HTML (minimal templates)
* **Configuration:** `.env` file

---

## 📂 Project Structure

```
auth-system/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not committed)
├── templates/          # HTML templates
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── README.md
```

---

## 🧱 Database Schema

The project uses a single `users` table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Design Notes

* Passwords are **never stored in plaintext**
* `bcrypt` automatically handles salting
* `username` is enforced as unique at the database level

---

## 🔐 Security Considerations

* Passwords are hashed using **bcrypt**, not SHA or plaintext
* Identical error messages are returned for invalid login attempts
* Secrets (DB credentials, Flask secret key) are stored in environment variables
* Sessions are used instead of storing auth state in the database

---

## ⚙️ Setup & Usage

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```
DB_HOST=127.0.0.1
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=auth_db
SECRET_KEY=your_secret_key
```

> ⚠️ The `.env` file is intentionally not committed to version control.

---

### 3️⃣ Initialize Database

Make sure MariaDB is running, then create the database and table using the provided schema.

---

### 4️⃣ Run the Application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000/
```

---

## 🧪 Manual Test Cases

* Register a new user
* Attempt duplicate registration
* Login with correct and incorrect credentials
* Access protected route without login
* Logout and verify session invalidation

---

## 🚀 Future Improvements

* Password strength validation
* Rate limiting for login attempts
* CSRF protection
* OAuth integration
* Dockerized deployment

---

## 🎯 What This Project Demonstrates

* Backend fundamentals and clean architecture
* Secure password handling practices
* Real-world database usage on Linux
* Environment-based configuration
* Debugging and system-level understanding (MariaDB auth, socket vs TCP)

---

## 📌 Note on Development Status

This project may be iteratively improved over time. Commits reflect incremental development and learning rather than a single polished release.

---

## 📄 License

This project is for educational purposes.
