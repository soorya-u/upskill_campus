# **Password Manager - upSkill Internship**


## Introduction

**Description**: The password manager is a Python project that securely stores and manages user passwords. It allows users to store their passwords for various accounts, generate strong passwords, and retrieve passwords when needed.

**Scope**: The scope of this project involves implementing encryption algorithms to secure password storage, designing a user interface to input and retrieve passwords, and developing functions to generate strong passwords and store/retrieve them from a database.

## Libraries Used

### Cryptography

`cryptography` is a package which provides cryptographic recipes and primitives in Python

In this Project, it is used to Encrypt and Decrypt User Passwords.

Installation (*in terminal*): `pip install cryptography`

Documentations:

- [*cryptography* Documentation](https://cryptography.io/en/latest/)

### Database

`MySQL` is very fast, reliable, and easy to use database system where the datas are stored in tables.

In this Project, it is used to store and maintain datas recieved from user.

Installation (*in terminal*): `pip install mysql-connector-python`

Documentations: 

- [*MySQL* Documentation](https://docs.oracle.com/en-us/iaas/mysql-database/doc/getting-started.html)

- [*mysql-connector-python* Documentation](https://dev.mysql.com/doc/connector-python/en/)

### Hashing

`hashlib` implements a common interface to many different secure hash and message digest algorithms.

In this Project, it is used to hash the Master Password and use it for Verification.

Documentation:

- [*hashlib* Documentation](https://docs.python.org/3/library/hashlib.html#)

### Graphical User Interface

`Tkinter` is the standard GUI library for a fast and easy way to create GUI applications.

In this Project, it is used to create a Simple Graphical User Interface for the Application.

Documentations:

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)