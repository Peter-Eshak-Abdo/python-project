from Library import Library

def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. Add Member")
        print("3. Add Section")
        print("4. List Books")
        print("5. List Members")
        print("6. List Section")
        print("7. Search Book")
        print("8. Search Member")
        print("9. Search Section")
        print("10. Exit")

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
            category = input("Enter category name: ")
            section_id = input("Enter Section ID: ")
            count = input("Enter the count: ")
            library.add_section(category, section_id, count)

        elif choice == "4":
            library.list_books()

        elif choice == "5":
            library.list_members()

        elif choice == "6":
            library.list_sections()

        elif choice == "7":
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                print("Book found:", book)
            else:
                print("Book not found.")

        elif choice == "8":
            name = input("Enter member name to search: ")
            # member_id = input("Enter member ID to search: ")
            # member = library.search_member(name, member_id)
            member = library.search_member(name)
            if member:
                print("Member found:", member)
            else:
                print("Member is not found.")


        elif choice == "9":
            category = input("Enter category name to search: ")
            section = library.search_section(category)
            if section:
                print("Section found:", section)
            else:
                print("Section is not found.")

        elif choice == "10":
            print("Exiting Library System.")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
