#GoodReads Clone

class book():
    def __init__(self,name,author,pages,published):
        self.name = name
        self.author = author
        self.pages = pages 
        self.published = published

    def displayBooks(self):
        return (
            f"Name: {self.name}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages}\n"
            f"Date published: {self.published}"
        )



book1 = book("Dungeon Crawler Carl","Matt Dimmons",873,"24 September 2026")

print(book1.displayBooks())