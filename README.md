# 🚀 **Account Management System**

This repository contains the implementation of an account creation and management system. It includes FastAPI routers that handle user signup, login, password recovery, account activation, deletion, and user data updates.

<br>

## 📖 Table of Contents

- 📌 [Project Overview](#project-overview)
- ⚙️ [Installation](#installation)
- 🛠️ [Technologies Used](#technologies-used)
- 📂 [File Structure](#file-structure)
- 📬 [Connect](#connect)

<br>
<a name="project-overview"></a>

## 📌 Project Overview

This Account Management System enables user-related functionalities, including:

- **User Signup**  
- **Login & Logout**  
- **Password Recovery**  
- **Account Activation & Deletion**  
- **User Data Update**

The goal of this system is to handle user authentication and management seamlessly.

> ⚠️ **Note:** These routes were developed for the **Maseer Project**. You can view its repository [here](https://github.com/NuhaMakki/MASEER_Traffic_Violation_Detection_System).

<br>
<a name="installation"></a>

## ⚙️ Installation

Follow these steps to set up and run this project:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NuhaMakki/Account_Management_System.git
cd Account_Management_System
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣  Configure Database Connection
Modify `database.py`  to match your MySQL configuration if needed:
```python
def connect_to_mysql():
    # Database configuration details
    config = {
        'host': 'localhost',
        'database': 'maseerdb',
        'user' : 'root',
        'password' : ''
    }
```

### 4️⃣ Run the FastAPI Server
```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000/`.

<br>
<a name="technologies-used"></a>

## 🛠️ Technologies Used

- 🐍 **Python**, ⚡ **FastAPI** – Backend & API  
- 🗄️ **MySQL** – Database  

<br>
<a name="file-structure"></a>

## 📂 File Structure

- **`main.py`**: FastAPI app entry point
- **`routers/`**: Contains FastAPI route handlers
  - **`signup.py`**: Handles user signup
  - **`login.py`**: Handles user login
  - **`password_recovery.py`**: Manages password recovery
  - **`updatePassword.py`**: Updates user password
  - **`updatePhone.py`**: Updates user phone number
  - **`userdata.py`**: Fetches and returns user profile data
  - **`sendEmail.py`**: Handles sending of verification and recovery emails
  - **`deleteAccount.py`**: Handles user account deletion
- **`models.py`**: Pydantic models for request/response validation
- **`database.py`**: MySQL configuration and queries
- **`requirements.txt`** – Python dependencies.
- **`README.md`** – Project documentation.
  
<br>
<a name="connect"></a>

## 📬 Connect

If you have any questions or suggestions, feel free to connect!

<div align="center">

<a href="mailto:noha.m.makki@gmail.com" rel="nofollow">
  <img align="left" alt="Nuha's Email" width="95px" src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"  style="max-width: 100%;">
</a>

<a href="https://www.linkedin.com/in/nuha-makki-a3b15a2b9/" rel="nofollow">
  <img align="left" alt="Nuha's LinkedIn" width="95px" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="max-width: 100%;">
</a>

<a href="https://github.com/NuhaMakki" rel="nofollow">
  <img align="left" alt="Nuha's GitHub" width="95px" src="https://img.shields.io/badge/GitHub-171515?style=for-the-badge&logo=github&logoColor=white"  style="max-width: 100%;">
</a>

</div>
