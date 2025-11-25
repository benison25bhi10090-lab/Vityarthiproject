**Simple Library Management System**

**Overview**

This is a small, easy-to-use command-line application that simulates the core operations of a library. It lets a user (or librarian) add books, list the library inventory, lend (issue) books, and accept returns. Data is stored in memory using Python lists and dictionaries for simplicity — ideal for learning and quick demos.
**Features**

-Add a new book (ID, title, author)
-Display all books with status (Available / Issued)
-Issue a book by its ID
-Return a book by its ID
-Starts with an optional preset list of books for quick testing
-Simple, easy-to-read code organized in functions

**Technologies / Tools Used
**Language:
-Python 3.x
-Standard library: sys, datetime
-Optional (for generating Word reports): python-docx

Installation & Setup

Install Python 3.x if it's not already installed:
Windows/macOS: download from https://www.python.org
Linux: use your package manager, e.g. sudo apt install python3
Create and activate a virtual environment:
(Optional) Install python-docx if you want to generate Word documents:
Place the project files in a folder. At minimum you should have:
library_management_simple.py
(optional) create_library_report_docx.py — script to generate a .docx report

How to Run

Run the main script from the command line:
python library_management_simple.py
You will see a menu similar to: ' *** Library Management System ***
Add Book
Display Books
Issue Book
Return Book
Exit Enter your choice (1-5): ` Follow the prompts to add, issue, return, or display books.
Example: Display books
Choose 2 at the menu prompt.
The program prints all books and their status:
ID: 1    Title: The Wimpikid    Author: Harper Lee    Status: Available
ID: 3    Title: Pride and Prejudice    Author: Jane Austen    Status: Issued
...
**Input Format / Examples
**
Book ID: treated as a string (e.g., 1, B101, A-23)
When asked to enter list of books (if you extend the program to accept bulk entry), supply space-separated values as prompted by the code.
Sample interactive session:
Menu choice: 1 (Add Book)
Book ID: 11
Book Title: New Book
Book Author: Some Author
Testing Manual tests
Test A: Add a new book and then choose Display Books to verify it is listed with status "Available".
Test B: Issue an available book (menu -> Issue) and confirm status changes to "Issued" and the ID is recorded in issued_books.
Test C: Try issuing a book already marked issued — an explanatory message should be shown.
Test D: Return an issued book and confirm it becomes available again.
Test E: Try returning a non-issued or non-existent ID — the program should show an appropriate message.

**Automated testing
**
Refactor core logic into functions that accept parameters instead of using input() directly.
Add unit tests using pytest. Example test outline:
test_add_book()
test_issue_book()
test_return_book()
test_cannot_issue_already_issued_book()
Suggested Improvements
Add input validation (prevent empty fields and duplicate IDs).
Persist data to a file (JSON / CSV) or a lightweight database (SQLite).
Track who borrowed a book and dates (borrower name, issue date, return date).
Implement search by title or author.
Add automated tests and continuous integration (GitHub Actions).
Optionally provide a small web UI or GUI for easier use.
