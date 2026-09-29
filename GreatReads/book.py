#GoodReads Clone
import os
import json

#Finds books.json next to this file, no matter which folder the program is run from.
BOOKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books.json")

def loadBooks():
    #Returns the list of book dicts from books.json, or an empty list if the file is missing/empty.
    if not os.path.exists(BOOKS_FILE) or os.path.getsize(BOOKS_FILE) == 0:
        return []
    with open(BOOKS_FILE, "r") as file:
        return json.load(file)
    print json.load(file[1])

def saveBooks(books):
    #Overwrites books.json with the full list of book dicts.
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

class book():
    def __init__(self,title,author,pages,published):
        self.title = title
        self.author = author
        self.pages = pages 
        self.published = published

    def displayBooks(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages}\n"
            f"Date published: {self.published}"
        )

    def book_to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "published": self.published
          #Converts inputed details in dict format. JSON supported.
        }
        
    
    def WriteToFile(self):
        #Loads the existing books, adds this one, and saves the list back.
        books = loadBooks()
        books.append(self.book_to_dict())
        saveBooks(books)



    def addNewBook():
        #Allows user to input book details to be entered.
        title = input("Enter title: ")
        author = input("Enter name of author: ")
        pages = input("Amount of page: ")
        published = input("Date published: ")

        book1 = book(title,author,pages,published)
        book1.book_to_dict()
        book1.WriteToFile()

    def searchBooks():
        #Finds books whose title contains the search term (case-insensitive).
        term = input("Enter part of the title: ").strip().lower()
        matches = [book(**data) for data in loadBooks() if term in data["title"].lower()]

        if matches:
            print(f"\nFound {len(matches)} match(es):\n")
            for match in matches:
                print(match.displayBooks() + "\n")
        else:
            print("No books found matching that title.")

        return matches

#TODO: Allow user to enter rating.
