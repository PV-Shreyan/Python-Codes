# Create a class Book that stores details like the title, author, and price of a book. Add methods to display the details of the book and apply a discount to the price.
# (a) Create two objects for different books and display their details.
# (b) Apply a 10% discount to one of the books and display the updated price.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

    def discount(self, percent):
        self.price -= self.price * (percent / 100)

b1 = Book("Book One", "Author A", 500)
b2 = Book("Book Two", "Author B", 300)

b1.display()
b2.display()

b1.discount(10)
print("After discount:")
b1.display()
