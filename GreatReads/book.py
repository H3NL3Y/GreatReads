#GoodReads Clone

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



def addNewBook():
    #Allows user to input book details to be entered.
    title = input("Enter title: ")
    author = input("Enter name of author: ")
    pages = input("Amount of page: ")
    published = input("Date published: ")

    book1 = book(title,author,pages,published)
    return book1


newBook = addNewBook()

#Converts new book to dict.
print(newBook.book_to_dict())
#TODO: Create menu system on main. 
#TODO: Allow user to enter rating.
#TODO: Store book details in JSON within the dict format.