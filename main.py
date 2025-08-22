from Library import Library

def main():

    while True:
        print("\n===== 📚 Library System =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. List Books")
        print("4. List Members")
        print("5. Search Book")
        print("6. Exit")

        choice = input("👉 Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter year: ")
            Library().add_book(title, author, year)

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            Library().add_member(name, member_id)

        elif choice == "3":
            Library().list_books()

        elif choice == "4":
            Library().list_members()

        elif choice == "5":
            title = input("Enter book title to search: ")
            book = Library().search_book(title)
            if book:
                print("✅ Book found:", book)
            else:
                print("❌ Book not found.")

        elif choice == "6":
            print("Exiting Library System.")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
