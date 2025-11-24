1.Problem Statement

​Traditional library management in small institutions often relies on manual record-keeping using paper ledgers or simple spreadsheets. This manual process presents several challenges:
​Inefficiency: Searching for a specific book or checking its status (Available vs. Issued) is time-consuming.
​Data Redundancy and Error: Manual entries often lead to duplicate records or lost data regarding who borrowed a book.
​Lack of Real-time Status: It is difficult to instantly determine if a book is currently on the shelf or with a student.
​The Solution: This project aims to solve these issues by developing a digital Library Management System. This software will automate the tracking of book inventory and the borrowing process, ensuring data accuracy and saving time for the librarian.

​2. Scope of the Project

​The scope of this project is to build a Command Line Interface (CLI) application using the Python programming language. The system focuses on the core "circulation" activities of a library.
​In-Scope:
​Management of book records (ID, Title, Author).
​Tracking the real-time status of books (Issued or Available).
​Automating the logic for issuing books to students.
​Handling the return process and updating inventory status.
​Validating inputs (e.g., preventing the issuing of an already issued book).
​Constraints:
​The current version uses volatile memory (Python lists/dictionaries) for data storage.
​The system is designed for a single administrative user (The Librarian).
​
3. Target Users

​Primary User (Administrator/Librarian):
​The person responsible for entering new books into the system.
​The person who manages the check-in and check-out process at the library desk.
​Secondary Stakeholders (Students/Faculty):
​While they do not interact with the software directly in this version, they are the beneficiaries of the faster service and accurate book availability information provided by the system.

​4. High-Level Features

​The system provides the following core functionalities:
​Book Acquisition (Add Book):
​Allows the librarian to input details of new books (ID, Title, Author).
​Automatically sets the default status of new books to "Available."
​Technical aspect: Implements the 'Create' part of CRUD operations.
​Catalog Viewing (Display Books):
​Provides a formatted, tabular view of all books in the library.
​Dynamically displays the status ("Issued" or "Available") based on current data.
​Technical aspect: Implements the 'Read' part of CRUD operations.
​Circulation Management (Issue Book):
​Allows the librarian to mark a book as borrowed using its unique ID.
​Includes validation logic to ensure a book cannot be issued if it is already out.
​Technical aspect: Implements the 'Update' part of CRUD operations.
​Inventory Recovery (Return Book):
​Updates the system when a student returns a book, making it available for others again.
​Includes error handling to ensure only currently issued books can be returned
