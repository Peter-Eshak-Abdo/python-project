from Book import books
from Member import members

class Library:
    def __init__(self):
        self.books = books
        self.members = members

    def add_book(self, title, author, year):
        book = books(title, author, year)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def add_member(self, name, member_id):
        member = members(name, member_id)
        self.members.append(member)
        print(f"Member '{name}' registered successfully.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                print(book)

    def list_members(self):
        if not self.members:
            print("No members registered.")
        else:
            print("\nMembers:")
            for member in self.members:
                print(member)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
