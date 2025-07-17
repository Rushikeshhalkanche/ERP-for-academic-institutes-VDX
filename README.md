# ERP-for-academic-institutes-VDX

# ERP for Academic Institutes - VDX

A backend ERP system built using Django and Django REST Framework to manage academic operations such as student records, exams, payments, and role-based authentication. The system is modular, scalable, and designed to integrate easily with any frontend.

---

## 🚀 Features

- 📘 Student Management (Add, Update, Delete, View)
- 🧾 Payment Module with:
  - Fee tracking
  - Auto-generated email receipts
  - Due payment reminders
- 📝 Exam Management (exam creation, student mapping)
- 🔐 Role-Based Access (Admin, Teacher, Student)
- 🧠 REST APIs built using Django REST Framework
- 📧 SMTP email integration for communication
- 📁 Clean project structure for scalability

---

## 🛠️ Tech Stack

- **Language**: Python 3.x  
- **Framework**: Django, Django REST Framework  
- **Database**: SQLite (development)  
- **Email**: SMTP (configured for sending receipts/reminders)  
- **Testing**: Postman  
- **Environment**: VS Code, Git

---

## 📂 Folder Structure

academic_erp/
├── students/
├── payments/
├── exams/
├── templates/
├── static/
├── media/
├── db.sqlite3
├── manage.py
└── ...
