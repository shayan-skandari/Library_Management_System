books = []


# ==========================
# Add Book
# ==========================

def add_book():
    title = input("Enter book title: ").strip()

    while not title:
        print("Title cannot be empty!")
        title = input("Enter book title: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            print("Book already exists!")
            return

    author = input("Enter author: ").strip()

    while not author:
        print("Author cannot be empty!")
        author = input("Enter author: ").strip()

    while True:
        try:
            year = int(input("Enter publication year: "))

            if year > 0:
                break
            else:
                print("Invalid year!")

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
        return

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
# Search Book
# ==========================

def search_book():
    title = input("Enter book title: ").strip()
    found = False

    for book in books:
        if book["title"].lower() == title.lower():
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
# Search by Author
# ==========================

def search_by_author():
    author = input("Enter author name: ").strip()
    found = False

    for book in books:
        if book["author"].lower() == author.lower():
            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])

            if book["available"]:
                print("Available")
            else:
                print("Borrowed")

    if not found:
        print("Author not found!")


# ==========================
# Edit Book
# ==========================

def edit_book():
    title = input("Enter book title to edit: ").strip()
    found = False

    for book in books:
        if book["title"].lower() == title.lower():
            found = True

            while True:
                new_title = input("Enter new title: ").strip()

                if new_title:
                    break

                print("Title cannot be empty!")

            book["title"] = new_title

            while True:
                new_author = input("Enter new author: ").strip()

                if new_author:
                    break

                print("Author cannot be empty!")

            book["author"] = new_author

            while True:
                try:
                    new_year = int(input("Enter new publication year: "))

                    if new_year > 0:
                        break
                    else:
                        print("Invalid year!")

                except ValueError:
                    print("Invalid year!")

            book["year"] = new_year

            print("Book updated successfully!")

    if not found:
        print("Book not found!")


# ==========================
# Count Books
# ==========================

def count_books():
    print(f"Total books: {len(books)}")


# ==========================
# Count Available Books
# ==========================

def count_available_books():
    count = 0

    for book in books:
        if book["available"]:
            count += 1

    print(f"Total available books: {count}")


# ==========================
# Count Borrowed Books
# ==========================

def count_borrowed_books():
    count = 0

    for book in books:
        if not book["available"]:
            count += 1

    print(f"Total borrowed books: {count}")


# ==========================
# Search by Year
# ==========================

def search_by_year():
    while True:
        try:
            year = int(input("Enter publication year: "))

            if year > 0:
                break
            else:
                print("Invalid year!")

        except ValueError:
            print("Invalid year!")

    found = False

    for book in books:
        if book["year"] == year:
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
# Search by Keyword
# ==========================

def search_by_keyword():
    keyword = input("Enter keyword: ").strip()

    found = False

    for book in books:
        if keyword.lower() in book["title"].lower():
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
# Clear Books
# ==========================

def clear_books():
    confirmation = input(
        "Are you sure you want to clear all books? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        books.clear()
        print("All books cleared successfully!")

    elif confirmation == "n":
        print("Clear operation cancelled!")

    else:
        print("Invalid choice!")

# ==========================
# Show Available Books
# ==========================

def show_available_books():
    found = False

    for book in books:
        if book["available"]:
            found = True


            print(book["title"])
            print(book["author"])
            print(book["year"])
            print("Available")


    if not found:
        print("No available books found!")        


# ==========================
# Show Borrowed Books
# ==========================

def show_borrowed_books():
    found = False

    for book in books:
        if not book["available"]:
            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])
            print("Borrowed")

    if not found:
        print("No borrowed books found!")

# ==========================
# Search By Availability
# ==========================

def search_by_availability():
    choice = input("Enter availability (available/borrowed): ").strip().lower()

    found = False

    for book in books:
        if choice == "available" and book["available"]:
            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])
            print("Available")

        elif choice == "borrowed" and not book["available"]:
            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])
            print("Borrowed")

    if not found:
        print("No books found!")

# ==========================
# Sort Books
# ========================== 

def sort_books():
    choice = input("Sort by (title/year): ").strip().lower()

    if choice == "title":
        books.sort(key=lambda book: book["title"].lower())

    elif choice == "year":
        books.sort(key=lambda book: book["year"])

    else:
        print("Invalid choice!")
        return

    print("Books sorted successfully!")

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
        print("10. Search Book")
        print("11. Search by Author")
        print("12. Edit Book")
        print("13. Count Books")
        print("14. Count Available Books")
        print("15. Count Borrowed Books")
        print("16. Search by Year")
        print("17. Search by Keyword")
        print("18. Clear Books")
        print("19. Show Available Books")
        print("20. Show Borrowed Books")
        print("21. Search By Availability")
        print("22. Sort Books")

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

        elif choice == "10":
            search_book()

        elif choice == "11":
            search_by_author()

        elif choice == "12":
            edit_book()

        elif choice == "13":
            count_books()

        elif choice == "14":
            count_available_books()

        elif choice == "15":
            count_borrowed_books()

        elif choice == "16":
            search_by_year()

        elif choice == "17":
            search_by_keyword()

        elif choice == "18":
            clear_books()

        elif choice == "19":
            show_available_books()  

        elif choice == "20":
            show_borrowed_books()      

        elif choice == "21":
            search_by_availability()

        elif choice == "22":
            sort_books()        


main_menu()

