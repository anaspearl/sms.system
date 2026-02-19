# 🎓 Smart Student Management System (SMS)

A modern, professional, and scalable Student Management System designed with clean architecture and Object-Oriented Programming (OOP) principles.

## 🚀 Overview

The **Smart Student Management System** provides a sleek interface for managing students, courses, and enrollments. It features a robust FastAPI backend combined with a premium, glassmorphism-inspired frontend to deliver a top-tier user experience.

## ✨ Features

- **📊 Dashboard Statistics**: Real-time overview of total students and active courses.
- **🙋 Student Registry**: Complete CRUD functionality (Create, Read, Update, Delete) for student records.
- **📚 Course Catalog**: Manage academic courses with specialized codes and descriptions.
- **🔗 Smart Enrollments**: 
    - Dynamic dropdown selection for students and courses.
    - Integrated search to view all enrollments for a specific student.
    - Simplified enrollment process with grade tracking.
- **🔔 Toast Notifications**: Professional feedback for every user action (Success, Error, Info).
- **🎨 Premium UI/UX**:
    - Modern Glassmorphism design system.
    - Responsive layout with smooth animations.
    - Intuitive, icon-based navigation.
- **⚡ Cache-Busting**: Integrated asset versioning to ensure users always have the latest features.

## 🛠️ Technology Stack

### Backend
- **Python**: Core logic.
- **FastAPI**: High-performance REST API.
- **SQLAlchemy**: ORM for database management.
- **Pydantic**: Data validation and serialization.
- **SQLite**: Reliable, lightweight database.
- **Uvicorn**: ASGI server.

### Frontend
- **Vanilla JavaScript**: Robust, dependency-free logic.
- **CSS3**: Modern styling with CSS variables and glassmorphism.
- **HTML5**: Semantic and accessible structure.
- **Google Fonts (Outfit)**: Premium typography.

## 🏃 Getting Started

### Prerequisites
- Python 3.8+
- `pip` (Python package manager)

### Installation
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

### Running the Application
Launch the server using the following command:
```bash
python app.py
```
The application will be available at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

## 📁 Project Structure

```text
ssms/
├── app.py              # FastAPI application & entry point
├── db.py               # Database configuration
├── models.py           # SQLAlchemy database models
├── managers.py         # Business logic & data management
├── static/             # Frontend assets
│   ├── index.html      # Main UI structure
│   ├── index.css       # Premium styles
│   └── script.js       # Frontend logic
└── student_management.db  # SQLite database file
```

## 🛡️ Reliability Improvements
This project has undergone significant refactoring to ensure:
- **ID-Safe Modals**: Handlers no longer rely on brittle inline serialization.
- **Dropdown Integration**: Manual ID entries replaced with dynamic selections.
- **Port Conflict Management**: Backend startup handles existing socket usage gracefully.
