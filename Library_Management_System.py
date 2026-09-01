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
    print(books)

    print("Book added successfully!")

add_book()