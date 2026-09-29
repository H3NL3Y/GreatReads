import sys
from book import book, loadBooks

#Menu stucture and linkage. 
print("Welcome to GreatReads!")
menu = input("""
                 1. Add new book
                 2. View all books
                 3. Search for a book
                 4. Exit
                 """)
if menu == "1":
        newBook = book.addNewBook()
elif menu == "2":
        for data in loadBooks():
            print(book(**data).displayBooks() + "\n")
elif menu == "3":
        book.searchBooks()
elif menu == "4":
        sys.exit()  
