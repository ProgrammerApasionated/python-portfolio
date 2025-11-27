def menu():
    print (".-"*30)
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display all books")
    print ("4.Show the number of pages")
    print ("5.Show available books")
    print ("6. Add a book to the library")
    print("7. Exit")
    print (".-"*30)
    choice = input("Enter your choice: ")
    return choice



class Book:
    def __init__(self, title, author, pages,available=True):
        self.title = title
        self.author = author
        self.pages = pages
        self.available = available

    def __str__(self):
        return f"The book {self.title} from the author {self.author} has {self.pages} pages"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"The library has {len(self.books)} books"
Book1 = Book