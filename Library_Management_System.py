books = []


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = int(input("Enter publication year: "))

    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(book)

    print("Book added successfully!")


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

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            show_books()


main_menu()
