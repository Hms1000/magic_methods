# Book class to store, title, author and pages of a book

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# using __str__ returns printed author,  title and pages of the book

    def __str__(self):
        return f'{self.title} by {self.author} ({self.pages})'

# returns length of the book
    
    def __len__(self):
        return self.pages
  
# checks if its a same book written by one author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# checks which book has more pages

    def __gt__(self, other):
        return self.pages > other.pages

# checks which book has less pages 
    def __lt__(self, other):
        return self.pages < other.pages
                  
book1 = Book('Black and white', 'Sam', 450)
book2 = Book('Countless Times', 'Pam', 620)
book3 = Book('Python essentials', 'Pam', 440)

print(str(book1))
print(str(book2))
print(str(book3))
print(book1 > book3) 
print(book1 < book2)
print(book3 > book1)
print(book1 == book2)
