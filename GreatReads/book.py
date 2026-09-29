#GoodReads Clone
import os

#Finds books.json next to this file, no matter which folder the program is run from.
BOOKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books.json")

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
        with open(BOOKS_FILE, "a") as file:
            file.write(str(self.book_to_dict()) + "\n")



    def addNewBook():
        #Allows user to input book details to be entered.
        title = input("Enter title: ")
        author = input("Enter name of author: ")
        pages = input("Amount of page: ")
        published = input("Date published: ")

        book1 = book(title,author,pages,published)
        book1.book_to_dict()
        book1.WriteToFile()
        
if __name__ == "__main__":
    menu = input("""
                 1. Add new book
                 2. View all books
                 3. Exit
                 """)
    if menu == "1":
        newBook = book.addNewBook()
    elif menu == "2":
        with open(BOOKS_FILE, "r") as file:
            for line in file:
                print(line)
    elif menu == "3":
        exit()
        
                 
                 



#TODO: Create menu system on main. 
#TODO: Allow user to enter rating.
#TODO: Store book details in JSON within the dict format.