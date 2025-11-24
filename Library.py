books = [{"id": "1", "title": "The Wimpikid", "author": "Harper Lee", "issued": False},
    {"id": "2", "title": "J", "author": "George Orwell", "issued": False},
    {"id": "3", "title": "Pride and Prejudice", "author": "Jane Austen", "issued": True},
    {"id": "4", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "issued": False},
    {"id": "5", "title": "Moby Dick", "author": "Herman Melville", "issued": True},
    {"id": "6", "title": "The Catcher in the Rye", "author": "J.D. Salinger", "issued": False},
    {"id": "7", "title": "Brave New World", "author": "Aldous Huxley", "issued": False},
    {"id": "8", "title": "The Hobbit", "author": "J.R.R. Tolkien", "issued": True},
    {"id": "9", "title": "The Odyssey", "author": "Homer", "issued": False},
    {"id": "10", "title": "The Alchemist", "author": "Paulo Coelho", "issued": False}]
issued_books = []

def add_book():
    print("\n Add a New Book ")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    })
    print(f"Book '{title}' by {author} (ID: {book_id}) added to the library.")

def display_books():
    print("\n Available Books ")
    if not books:
        print("No books in the library yet.")
        return
    for book in books:
        if book["issued"]:
          status = "Issued"
        else:
          status = "Available"

        print(f'ID: {book["id"]}\tTitle: {book["title"]}\tAuthor: {book["author"]}\tStatus: {status}')

def issue_book():
    print("\n Issue a Book ")
    book_id = input("Enter the Book ID to issue: ")
    for book in books:
        if book["id"] == book_id:
            if not book["issued"]:
                book["issued"] = True
                issued_books.append(book_id)
                print(f" The the book is issued '{book['title']}' Written by {book['author']}.")
                return
            else:
                print("Sorry, that book is already issued.")
                return
    print("Sorry, book not found in the library.")

def return_book():
    print("\n Return a Book ")
    book_id = input("Enter the Book ID to return: ")
    if book_id in issued_books:
        for book in books:
            if book["id"] == book_id:
                book["issued"] = False
                issued_books.remove(book_id)
                print(f"Thank you for returning '{book['title']}'.")
                return
    print("No record of this book being issued. Recheck the Book ID.")

def menu():
    while True:
        print("\n*** Library Management System ***")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print(" Thank you , Have a nice day ")
            break
        else:
            print("INCORRECT choice, Enter a number from 1 to 5:")
if __name__ == "__main__":
    menu()