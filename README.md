# E-Resource Management System

Welcome to the **E-Resource Management System**! This project is designed to manage educational resources, including question banks, solutions, and eBooks. Users can access, download, and manage various educational materials through this system.

## Features

- **Question Bank**: Browse and search through a comprehensive question bank.
- **Solutions**: Access detailed solutions to various problems and questions.
- **eBooks**: Download educational eBooks for study and reference.
- **PYQ (Previous Year Questions)**: Access previous year’s question papers for practice.

## Installation

To set up and run the E-Resource Management System locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ladyunicorn560/E-resource_management_system.git
   cd E-resource_management_system
python -m venv env
.\env\Scripts\activate


pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
