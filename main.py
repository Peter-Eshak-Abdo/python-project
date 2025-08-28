from Library import Library

def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. Add Member")
        print("3. List Books")
        print("4. List Members")
        print("5. Search Book")
        print("6. Search Member")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter year: ")
            library.add_book(title, author, year)

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.add_member(name, member_id)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            library.list_members()

        elif choice == "5":
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                print("Book found:", book)
            else:
                print("Book not found.")

        elif choice == "6":
            name = input("Enter member name to search: ")
            # member_id = input("Enter member ID to search: ")
            # member = library.search_member(name, member_id)
            member = library.search_member(name)
            if member:
                print("Member found:", member)
            else:
                print("Member is not found.")

        elif choice == "7":
            print("Exiting Library System.")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
