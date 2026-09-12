import datetime

books = []


borrow_history = []

# ==========================
# Add Book
# ==========================

def add_book():

    title = input("Enter book title: ").strip()

    if not title:
        print("Title cannot be empty!")
        return

    author = input("Enter author name: ").strip()

    if not author:
        print("Author cannot be empty!")
        return

    try:
        year = int(input("Enter publication year: "))
    except ValueError:
        print("Year must be a number!")
        return

    if year <= 0:
        print("Year must be greater than 0!")
        return

    for book in books:

        if book["title"].lower() == title.lower():
            print("Book already exists!")
            return

    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True,
        "borrower": ""
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
            print("Borrower:", book["borrower"])

        print("-" * 30)



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
                print("Borrower:", book["borrower"])

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

            found = True

            print("Book deleted successfully!")

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

                borrower = input("Enter borrower name: ")

                book["borrower"] = borrower
                book["available"] = False

                history = {
                    "title": book["title"],
                    "borrower": borrower,
                    "action": "Borrowed",
                    "date": datetime.datetime.now()
                }

                borrow_history.append(history)

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

                borrower = book["borrower"]

                history = {
                    "title": book["title"],
                    "borrower": borrower,
                    "action": "Returned",
                    "date": datetime.datetime.now()
                }

                borrow_history.append(history)

                book["available"] = True
                book["borrower"] = ""

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
                f"{book['borrower']}\n"
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

            title, author, year, available, borrower = line.strip().split("|")

            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "available": available == "True",
                "borrower": borrower
            }

            books.append(book)

    print("Books loaded successfully!")



# ==========================
# Search Book
# ==========================

def search_books():

    search_type = input("Search by (title/author/year): ").strip().lower()

    if search_type == "title":
        search_value = input("Enter book title: ").strip()

    elif search_type == "author":
        search_value = input("Enter author name: ").strip()

    elif search_type == "year":
        search_value = int(input("Enter publication year: "))

    else:
        print("Invalid search type!")
        return

    found = False

    for book in books:

        if search_type == "title":

            if book["title"].lower() == search_value.lower():
                found = True

        elif search_type == "author":

            if book["author"].lower() == search_value.lower():
                found = True

        elif search_type == "year":

            if book["year"] == search_value:
                found = True

        if found:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])

            if book["available"]:
                print("Available")
            else:
                print("Borrowed")
                print("Borrower:", book["borrower"])

            print("------------------------------")

            found = False

    if not found:
        print("No books found!")


# ==========================
# Search by Author
# ==========================

def search_by_author():

    author = input("Enter author name: ").strip().lower()

    found = False

    for book in books:

        if author in book["author"].lower():

            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])

    if not found:
        print("No books found!")



# ==========================
# Edit Book
# ==========================

def edit_book():

    title = input("Enter book title: ").strip()

    found = False

    for book in books:

        if book["title"] == title:

            found = True

            new_title = input("Enter new title: ").strip()

            if new_title:
                book["title"] = new_title

            new_author = input("Enter new author: ").strip()

            if new_author:
                book["author"] = new_author

            try:
                new_year = int(input("Enter new publication year: "))

            except ValueError:
                print("Year must be a number!")
                return

            if new_year <= 0:
                print("Year must be greater than 0!")
                return

            book["year"] = new_year

            print("Book updated successfully!")

    if not found:
        print("Book not found!")



# ==========================
# Count Books
# ==========================

def count_books():

    print("Total books:", len(books))



# ==========================
# Count Available Books
# ==========================

def count_available_books():

    count = 0

    for book in books:

        if book["available"]:
            count += 1

    print("Available books:", count)



# ==========================
# Count Borrowed Books
# ==========================

def count_borrowed_books():

    count = 0

    for book in books:

        if not book["available"]:
            count += 1

    print("Borrowed books:", count)



# ==========================
# Search by Year
# ==========================

def search_by_year():

    try:
        year = int(input("Enter publication year: "))

    except ValueError:
        print("Year must be a number!")
        return

    found = False

    for book in books:

        if book["year"] == year:

            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])

    if not found:
        print("No books found!")



# ==========================
# Search by Keyword
# ==========================

def search_by_keyword():

    keyword = input("Enter keyword: ").strip().lower()

    found = False

    for book in books:

        if (
            keyword in book["title"].lower()
            or keyword in book["author"].lower()
        ):

            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])

    if not found:
        print("No books found!")



# ==========================
# Clear Books
# ==========================

def clear_books():

    if not books:
        print("No books found!")
        return

    confirm = input(
        "Are you sure you want to delete all books? (yes/no): "
    ).strip().lower()

    if confirm == "yes":

        books.clear()

        print("All books cleared!")

    else:

        print("Clear cancelled.")



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

            print("-" * 30)

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
            print("Borrower:", book["borrower"])

            print("-" * 30)

    if not found:
        print("No borrowed books found!")



# ==========================
# Search by Availability
# ==========================

def search_by_availability():

    availability = input(
        "Enter availability (available/borrowed): "
    ).strip().lower()

    found = False

    for book in books:

        if availability == "available":

            match = book["available"]

        elif availability == "borrowed":

            match = not book["available"]

        else:

            print("Invalid availability!")
            return

        if match:

            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])

            if book["available"]:

                print("Available")

            else:

                print("Borrowed")
                print("Borrower:", book["borrower"])

            print("-" * 30)

    if not found:
        print("No books found!")



# ==========================
# Sort Books
# ==========================

def sort_books():

    books.sort(
        key=lambda book: book["title"].lower()
    )

    print("Books sorted successfully!")



# ==========================
# Filter Books by Year
# ==========================

def filter_books_by_year():

    try:

        year = int(
            input("Enter minimum publication year: ")
        )

    except ValueError:

        print("Year must be a number!")
        return

    found = False

    for book in books:

        if book["year"] >= year:

            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])

            if book["available"]:

                print("Available")

            else:

                print("Borrowed")
                print("Borrower:", book["borrower"])

            print("-" * 30)

    if not found:

        print("No books found!")



# ==========================
# Filter Books
# ==========================

def filter_books():

    try:

        year = int(
            input("Enter minimum publication year: ")
        )

    except ValueError:

        print("Year must be a number!")
        return

    availability = input(
        "Enter availability (available/borrowed): "
    ).strip().lower()

    found = False

    for book in books:

        year_match = book["year"] >= year

        if availability == "available":

            availability_match = book["available"]

        elif availability == "borrowed":

            availability_match = not book["available"]

        else:

            print("Invalid availability!")
            return

        if year_match and availability_match:

            found = True

            print(book["title"])
            print(book["author"])
            print(book["year"])

            if book["available"]:

                print("Available")

            else:

                print("Borrowed")
                print("Borrower:", book["borrower"])

            print("-" * 30)

    if not found:

        print("No books found!")


# ==========================
# Change Borrowed
# ==========================

def change_borrower():

    title = input("Enter book title: ").strip()

    found = False

    for book in books:

        if book["title"] == title:
            found = True

            if not book["available"]:

                new_borrower = input("Enter new borrower name: ")

                book["borrower"] = new_borrower

                print("Borrower updated successfully!")

            else:
                print("Book is not borrowed!")

    if not found:
        print("Book not found!")            
                

# ==========================
# Show Borrow History
# ==========================

def show_borrow_history():

    for history in borrow_history:

        print("Book:", history["title"])
        print("Borrower:", history["borrower"])
        print("Action:", history["action"])
        print("Date:", history["date"])
        print("------------------------------")


# ==========================
# Clear borrow history
# ==========================

def clear_borrow_history():

    confirmation = input("Are you sure you want to clear borrow history? (yes/no): ")


    if confirmation == "yes":
        borrow_history.clear()
        print("Borrow history cleared successfully!")
    else:
        print("Borrow history was not cleared")


# ==========================
# Sort Books
# ==========================    

def sort_books():

    sort_type = input("Sort by (title/author/year): ").strip().lower()

    if sort_type == "title":
        sorted_books = sorted(
            books,
            key=lambda book: book["title"]
        )

    elif sort_type == "author":
        sorted_books = sorted(
            books,
            key=lambda book: book["author"]
        )

    elif sort_type == "year":
        sorted_books = sorted(
            books,
            key=lambda book: book["year"]
        )

    else:
        print("Invalid sort type!")
        return

    for book in sorted_books:
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])

        if book["available"]:
            print("Available")
        else:
            print("Borrowed")
            print("Borrower:", book["borrower"])

        print("------------------------------")   

# ==========================
# Menu
# ==========================

while True:

    print("\n===== Library Management System =====")

    print("1. Add Book")
    print("2. Show Books")
    print("3. Show Book")
    print("4. Delete Book")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")
    print("8. Save Books")
    print("9. Load Books")
    print("10. Search Books")
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
    print("21. Search by Availability")
    print("22. Sort Books")
    print("23. Filter Books by Year")
    print("24. Filter Books")
    print("25. Change Borrower")
    print("26. Show Borrow History")
    print("27. Clear Borrow History")
    print("28. Sort books")

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

        print("GoodBye!")
        break


    elif choice == "8":

        save_books()


    elif choice == "9":

        load_books()


    elif choice == "10":

        search_books()


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


    elif choice == "23":

        filter_books_by_year()


    elif choice == "24":

        filter_books()

    elif choice == "25":
        change_borrower()  

    elif choice == "26":
        show_borrow_history()  

    elif choice == "27":
        clear_borrow_history()

    elif choice == "28":
        sort_books()            


    else:

        print("Invalid choice!")

