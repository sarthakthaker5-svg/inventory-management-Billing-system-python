<div align="center">

# 🏪 Inventory Management System

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=28&duration=3000&pause=1000&color=36BCF7&center=true&vCenter=true&width=750&lines=Inventory+Management;Billing+System;Stock+Management;Python+Desktop+Application" alt="Typing SVG" />

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Tkinter-GUI-FFB000?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-Data%20Handling-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenPyXL-Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge"/>

<br><br>

*A desktop-based Inventory Management and Billing System developed using Python, Tkinter and SQLite to manage products, employees, suppliers, categories, sales and customer billing.*

</div>

---

# 📖 Project Overview

**Inventory Management System (IMS)** is a Python-based desktop application designed to simplify inventory, stock and billing operations for a small business or retail environment.

The system provides a graphical user interface using **Tkinter** and stores application data in an **SQLite database**.

The application includes modules for managing **Employees, Suppliers, Categories, Products, Sales and Billing**. It also provides login functionality and a dashboard that displays important inventory information.

The project demonstrates practical implementation of Python GUI development, database management, CRUD operations, searching, billing, authentication and Excel-based bill handling.

---

# 🎯 Objectives

* Develop a desktop-based inventory management application.
* Manage product and stock information efficiently.
* Maintain employee records.
* Manage supplier information.
* Organize products using categories.
* Generate and manage customer bills.
* Maintain sales records.
* Provide login-based access to the system.
* Store application data using SQLite.
* Practice Python GUI and database programming.
* Provide a simple and user-friendly interface for inventory operations.

---

# ✨ Project Highlights

* ✔ Python-based desktop application.
* ✔ Tkinter graphical user interface.
* ✔ SQLite database integration.
* ✔ Employee management.
* ✔ Supplier management.
* ✔ Product management.
* ✔ Category management.
* ✔ Sales management.
* ✔ Customer billing system.
* ✔ Login authentication.
* ✔ Admin and employee user types.
* ✔ Product search functionality.
* ✔ Supplier and category search.
* ✔ Employee search.
* ✔ Invoice search.
* ✔ Add, update and delete operations.
* ✔ Stock quantity management.
* ✔ Product status management.
* ✔ Excel-based billing records.
* ✔ Dashboard with inventory statistics.
* ✔ Automatic date and time display.

---

# 🛠️ Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Application Development             |
| Tkinter      | Graphical User Interface            |
| SQLite       | Database Management                 |
| Pandas       | Reading and displaying billing data |
| OpenPyXL     | Excel file creation and handling    |
| Pillow (PIL) | Image processing and GUI images     |
| SMTP         | Email-related functionality         |
| OS Module    | File and directory management       |

---

# 📂 Project Structure

```text
Inventory-Management-System/
│
├── dashboard.py
├── login.py
├── create_db.py
├── employee.py
├── supplier.py
├── category.py
├── product.py
├── sales.py
├── billing.py
├── ims.db
│
├── billing/
│   └── Excel billing files
│
├── bill/
│   └── Bill records
│
├── Image/
│   ├── Logo.png
│   ├── Menu.png
│   ├── Login.jpg
│   ├── signup.png
│   ├── socialmedia.png
│   └── Other project images
│
├── Documentation.docx
├── PPT.pptx
└── README.md
```

---

# 🗃️ Database Information

| Property             | Details             |
| -------------------- | ------------------- |
| Database Name        | `ims.db`            |
| Database Type        | Relational Database |
| DBMS                 | SQLite              |
| Programming Language | Python              |
| GUI Framework        | Tkinter             |
| Database Tables      | 4                   |

---

# 🗄️ Database Tables

The application uses an SQLite database named **ims.db**.

## 👨‍💼 Employee Table

Stores employee and user information.

| Field   | Description     |
| ------- | --------------- |
| eid     | Employee ID     |
| name    | Employee Name   |
| email   | Email Address   |
| gender  | Gender          |
| contact | Contact Number  |
| dob     | Date of Birth   |
| doj     | Date of Joining |
| pass    | Password        |
| utype   | User Type       |
| address | Address         |
| salary  | Salary          |

---

## 🚚 Supplier Table

Stores supplier information.

| Field   | Description          |
| ------- | -------------------- |
| invoice | Supplier Invoice ID  |
| name    | Supplier Name        |
| contact | Supplier Contact     |
| desc    | Supplier Description |

---

## 🏷️ Category Table

Stores product categories.

| Field | Description   |
| ----- | ------------- |
| cid   | Category ID   |
| name  | Category Name |

---

## 📦 Product Table

Stores product and stock information.

| Field    | Description      |
| -------- | ---------------- |
| pid      | Product ID       |
| Supplier | Supplier Name    |
| Category | Product Category |
| name     | Product Name     |
| price    | Product Price    |
| qty      | Product Quantity |
| status   | Product Status   |

---

# ✨ Main Features

## 🔐 Login System

The application provides a login screen where users can enter:

* Login ID
* Password

The system checks the entered credentials against the employee records stored in the SQLite database.

Different user types can access different parts of the system.

---

## 📊 Dashboard

The dashboard provides an overview of the inventory system.

It displays:

* 👨‍💼 Total Employees
* 🚚 Total Suppliers
* 🏷️ Total Categories
* 📦 Total Products
* 💰 Total Sales

The dashboard also displays the current date and time.

---

## 👨‍💼 Employee Management

The Employee module allows the administrator to manage employee information.

### Operations

* Add employee
* Update employee
* Delete employee
* Search employee
* Clear employee information

### Employee Information

* Employee ID
* Name
* Gender
* Contact
* Date of Birth
* Date of Joining
* Email
* Password
* User Type
* Address
* Salary

---

## 🚚 Supplier Management

The Supplier module manages supplier information.

### Operations

* Add supplier
* Update supplier
* Delete supplier
* Search supplier
* Clear supplier information

Supplier records include:

* Invoice Number
* Supplier Name
* Contact
* Description

---

## 🏷️ Category Management

The Category module allows users to organize products into categories.

### Operations

* Add category
* Delete category
* View categories
* Select category

---

## 📦 Product Management

The Product module manages inventory products and their stock details.

### Product Information

* Product ID
* Category
* Supplier
* Product Name
* Price
* Quantity
* Status

### Operations

* Add product
* Update product
* Delete product
* Search product
* Clear product information

### Product Status

Products can have statuses such as:

* Active
* Inactive

---

## 🧾 Billing System

The Billing module provides a customer billing interface.

Users can:

* Search products.
* Select products.
* Enter quantities.
* Add products to the cart.
* Generate customer bills.
* Calculate billing information.
* Save billing records.
* Print bills.

The system also maintains billing files for later reference.

---

## 💰 Sales Management

The Sales module allows users to view previously generated customer bills.

Users can:

* View sales records.
* Search using invoice number.
* Display billing information.
* Clear the current search.

Billing information can be read from stored Excel files.

---

# 🔄 CRUD Operations

The project demonstrates CRUD operations across multiple modules.

| Operation | Description             |
| --------- | ----------------------- |
| Create    | Add new records         |
| Read      | View and search records |
| Update    | Modify existing records |
| Delete    | Remove records          |

CRUD operations are implemented for important inventory entities such as:

* Employees
* Suppliers
* Categories
* Products

---

# 🔍 Search Functionality

The application provides search functionality for different modules.

### Employee Search

Search employees using:

* Name
* Email
* Contact

### Product Search

Search products using:

* Category
* Supplier
* Product Name

### Supplier Search

Search suppliers using invoice number.

### Sales Search

Search customer bills using invoice number.

---

# 📊 Dashboard Statistics

The dashboard automatically retrieves information from the SQLite database and displays inventory statistics.

The system calculates the number of:

```text
Employees
Suppliers
Categories
Products
Sales
```

This provides a quick overview of the current system status.

---

# 📁 Billing & Excel Integration

The application uses **OpenPyXL** to create and handle Excel-based billing records.

The billing module can save customer billing information into Excel files.

The Sales module uses **Pandas** to read stored Excel billing files and display their contents inside the application.

This provides an easy way to maintain and review sales records.

---

# 🖥️ User Interface

The application contains multiple graphical interfaces developed using Tkinter.

Main screens include:

* 🔐 Login Screen
* 📊 Dashboard
* 👨‍💼 Employee Management
* 🚚 Supplier Management
* 🏷️ Category Management
* 📦 Product Management
* 💰 Sales Management
* 🧾 Billing System

The project also uses images and icons to improve the visual appearance of the application.

---

# 📸 Project Screenshots

Add your screenshots to the `Image` folder and use them in this section.

## 🔐 Login Screen

<p align="center">
  <img src="Login.jpg" width="900" alt="Login Screen">
</p>

---

## 📊 Dashboard

<p align="center">
  <img src="Menu.png" width="900" alt="Dashboard">
</p>

---

## 🏷️ Category Management

<p align="center">
  <img src="Cat.jpg" width="900" alt="Category Management">
</p>

---

# 🔑 Python Concepts Used

The project demonstrates several Python programming concepts:

* Variables
* Functions
* Classes
* Object-Oriented Programming
* Conditional Statements
* Loops
* Exception Handling
* File Handling
* Database Connectivity
* GUI Programming
* Event Handling
* Modules and Imports

---

# 🧠 Database Concepts Used

The project demonstrates:

* SQLite database creation
* Table creation
* Primary Keys
* Foreign Keys
* INSERT operations
* SELECT operations
* UPDATE operations
* DELETE operations
* WHERE conditions
* Database relationships
* Database queries

---

# 🏗️ Application Architecture

The application follows a modular structure where different Python files handle different parts of the system.

```text
                    ┌─────────────────────┐
                    │     Login System    │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
              Admin                       Employee
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐          ┌──────────────┐
        │    Dashboard    │          │    Billing   │
        └────────┬────────┘          └──────────────┘
                 │
     ┌───────────┼───────────┬───────────┬───────────┐
     ▼           ▼           ▼           ▼           ▼
 Employee    Supplier    Category     Product      Sales
     │           │           │           │           │
     └───────────┴───────────┴─────┬─────┴───────────┘
                                   ▼
                            ┌─────────────┐
                            │   SQLite    │
                            │  ims.db     │
                            └─────────────┘
```

---

# 🚀 How to Run

## Step 1 — Install Python

Install Python 3.x on your computer.

Check the installation:

```bash
python --version
```

---

## Step 2 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then move into the project folder:

```bash
cd Inventory-Management-System
```

---

## Step 3 — Install Required Libraries

Install the required Python packages:

```bash
pip install pillow pandas openpyxl
```

Tkinter is normally included with standard Python installations on Windows.

---

## Step 4 — Create the Database

Run:

```bash
python create_db.py
```

This creates the SQLite database:

```text
ims.db
```

and the required tables.

---

## Step 5 — Run the Application

Start the login system:

```bash
python login.py
```

The login window will open.

---

# 🔑 Default Login

Use the employee credentials stored in the `ims.db` database.

If the database is newly created, add an employee record through the database before attempting to log in.

> **Note:** Do not upload real passwords or sensitive credentials to a public GitHub repository.

---

# 📌 Important Notes

* Keep `ims.db` in the same project directory as the Python files.
* Keep the `Image` folder in the project directory.
* Keep the `billing` folder available for billing records.
* Run the application from the project directory so relative file paths work correctly.
* Some existing code paths may need to be updated when moving the project to another computer.

---

# 🎓 Learning Outcomes

After completing this project, I gained practical experience in:

* Python programming.
* Object-Oriented Programming.
* Tkinter GUI development.
* SQLite database management.
* CRUD operations.
* Database connectivity.
* Inventory management.
* Billing system development.
* File handling.
* Excel file processing.
* Pandas data handling.
* GUI event handling.
* User authentication.
* Modular Python programming.
* Building a complete desktop application.

---

# 💼 Skills Demonstrated

### Programming Skills

* Python
* Object-Oriented Programming
* Exception Handling
* File Handling
* Modular Programming

### Database Skills

* SQLite
* Database Design
* CRUD Operations
* Primary Keys
* Foreign Keys
* SQL Queries

### GUI Skills

* Tkinter
* Forms
* Buttons
* Labels
* Entry Fields
* ComboBoxes
* Tables
* Scrollbars
* Message Boxes
* Multiple Windows

### Data Handling Skills

* Pandas
* OpenPyXL
* Excel File Handling
* Billing Data Processing

---

# 🏆 Project Achievements

✅ Developed a complete desktop-based Inventory Management System.

✅ Implemented a graphical interface using Tkinter.

✅ Integrated SQLite for database management.

✅ Implemented employee management.

✅ Implemented supplier management.

✅ Implemented category management.

✅ Implemented product and stock management.

✅ Developed customer billing functionality.

✅ Implemented sales record management.

✅ Added search functionality across multiple modules.

✅ Implemented login authentication.

✅ Integrated Excel-based billing records.

---

# 🔮 Future Enhancements

The system can be further improved by adding:

### 🔐 Security Enhancements

* Password hashing using `bcrypt`.
* Improved authentication.
* Role-Based Access Control.
* Secure password recovery.
* Session management.

### 📦 Inventory Enhancements

* Low-stock alerts.
* Automatic stock updates after sales.
* Stock history.
* Product barcode scanning.
* Inventory reports.

### 📊 Reporting Enhancements

* Sales charts.
* Monthly sales reports.
* Profit and loss analysis.
* Inventory reports.
* Export reports to PDF and Excel.

### ☁️ System Enhancements

* Cloud database integration.
* Multi-user support.
* Web-based version.
* Mobile-friendly interface.
* Automated backup system.

---

# 📌 Project Summary

**Inventory Management System** is a Python-based desktop application developed to manage inventory, products, suppliers, employees, categories, sales and customer billing.

The project combines **Python, Tkinter, SQLite, Pandas and OpenPyXL** to create a practical business management application.

It demonstrates how Python can be used to develop a complete desktop application with a graphical interface, database connectivity, CRUD operations, authentication, inventory management and billing functionality.

---

# 👨‍💻 Author

## Sarth Thakar

