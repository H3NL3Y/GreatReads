import json,sys,os
from book import book
BOOKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books.json")

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
        with open(BOOKS_FILE, "r") as file:
            for line in file:
                print(line)
elif menu == "3":
        pass
elif menu == "4":
        sys.exit()  
