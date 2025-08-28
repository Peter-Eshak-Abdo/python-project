from Book import books
from Book import Book
from Member import members
from Member import Member
from Section import sections
from Section import Section

class Library:
    def __init__(self):
        self.books = books
        self.members = members
        self.sections = sections

    def add_book(self, title, author, year):
        # book = books(title, author, year)
        book = Book(title, author, year)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def add_member(self, name, member_id):
        # member = members(name, member_id)
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Member '{name}' registered successfully.")

    def add_section(self, category , section_id, count):
        section = Section(category , section_id, count)
        self.sections.append(section)
        print(f"Section '{category}' registered successfully.")

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

    def list_sections(self):
        if not self.sections:
            print("No Section Found.")
        else:
            print("\Sections:")
            for section in self.sections:
                print(section)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

    def search_member(self, name, member_id):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member

    def search_section(self, category):
        for section in self.sections:
            if section.category.lower() == category.lower():
                return category
