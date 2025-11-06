class Book_Shop:

    # constructor
    def __init__(self, title , price):
        self.title = title
        self.price = price

    def book(self):
        print(f"Title: {self.title}, Price: {self.price}")

b = Book_Shop('Sandman', '$199')        
b.book()