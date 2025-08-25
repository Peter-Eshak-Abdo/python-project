
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year =year
        self.Not_available = False

    def Notavailable(self):
        if not self.Not_available:
            self.Not_available = True
            return True
        return False

    def return_book(self):
        if self.Not_available :
            self.Not_available = False
            return True
        return False

    def __str__(self):
        return f"\nTitle: {self.title} ,Auther: {self.author} ,Year: {self.year}\n"

books = [
    Book("1984", "George Orwell", 2000),
    Book("Brave New World", "Aldous Huxley", 2000)
]
