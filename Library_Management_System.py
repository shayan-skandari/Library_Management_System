books = []


# ==========================
# Add Book
# ==========================

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()

    while True:
        try:
            year = int(input("Enter publication year: "))
            break
        except ValueError:
            print("Invalid year!")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(book)

    print("Book added successfully!")

# ==========================
# Show Books
# ==========================

def show_books():
    if not books:
        print("No books found!")

    for book in books:
        print(book["title"])
        print(book["author"])
        print(book["year"])

        if book["available"]:
            print("Available")
        else:
            print("Borrowed")


# ==========================
# Show Book
# ==========================

def show_book():
    title = input("Enter book title: ").strip()
    found = False

    for book in books:
        if book["title"] == title:
            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])

            if book["available"]:
                print("Available")
            else:
                print("Borrowed")

    if not found:
        print("Book not found!")


# ==========================
# Delete Book
# ==========================

def delete_book():
    title = input("Enter book title: ").strip()
    found = False

    for book in books:
        if book["title"] == title:
            books.remove(book)
            print("Book deleted successfully!")
            found = True
            break

    if not found:
        print("Book not found!")


# ==========================
# Borrow Book
# ==========================

def borrow_book():
    title = input("Enter book title: ").strip()
    found = False

    for book in books:
        if book["title"] == title:
            found = True

            if book["available"]:
                book["available"] = False
                print("Book borrowed successfully!")
            else:
                print("Book is already borrowed!")

    if not found:
        print("Book not found!")


# ==========================
# Return Book
# ==========================

def return_book():
    title = input("Enter book title: ").strip()
    found = False

    for book in books:
        if book["title"] == title:
            found = True

            if not book["available"]:
                book["available"] = True
                print("Book returned successfully!")
            else:
                print("Book is already available!")

    if not found:
        print("Book not found!")


# ==========================
# Save Books
# ==========================

def save_books():
    with open(
        r"C:\Users\Shayan\Desktop\python_project\Library_Management_System\books.txt",
        "w"
    ) as file:

        for book in books:
            file.write(
                f"{book['title']}|{book['author']}|"
                f"{book['year']}|{book['available']}\n"
            )

    print("Books saved successfully!")


# ==========================
# Load Books
# ==========================

def load_books():
    books.clear()

    with open(
        r"C:\Users\Shayan\Desktop\python_project\Library_Management_System\books.txt",
        "r"
    ) as file:

        for line in file:
            title, author, year, available = line.strip().split("|")

            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "available": available == "True"
            }

            books.append(book)

    print("Books loaded successfully!")


# ==========================
# Main Menu
# ==========================

def main_menu():
    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Show Book")
        print("4. Delete Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        print("8. Save Books")
        print("9. Load Books")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            show_books()

        elif choice == "3":
            show_book()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            borrow_book()

        elif choice == "6":
            return_book()

        elif choice == "7":
            print("Goodbye!")
            break

        elif choice == "8":
            save_books()

        elif choice == "9":
            load_books()


main_menu()
