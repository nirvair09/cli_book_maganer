def main():
    # Initialize the book list
    bookList = []

    # Try to open and read the existing book list from a file
    try:
        infile = open("theBookList.txt", "r")
        line = infile.readline()
        while line:
            # Split each line by comma and add to the book list
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        # If the file is not found, initialize an empty book list
        print("theBookList.txt not found in the computer")
        print("Starting a new bookList")

    choice = 0
    while choice != 4:
        # Display the menu options
        print("***Book Manager***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display all books")
        print("4) Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Add a new book to the list
            print("Adding a book...")
            nBook = input("Enter the name of the book >>> ")
            nAuthor = input("Enter the name of the author >>> ")
            nPages = input("Enter number of pages >>> ")
            bookList.append([nBook, nAuthor, nPages])

        elif choice == 2:
            # Look up a book by a keyword
            print("Looking up for a book...")
            keyword = input("Enter search term >>> ")
            found = False
            for book in bookList:
                if any(keyword in item for item in book):
                    print(book)
                    found = True
            if not found:
                print("No book found with the given keyword.")

        elif choice == 3:
            # Display all books in the list
            print("Displaying all books...")
            for book in bookList:
                print(book)

        elif choice == 4:
            # Exit the program
            print("Quitting program...")

        else:
            print("Invalid choice. Please choose a valid option.")

    print("Program terminated successfully")

    # Save the updated book list to an external file
    with open("theBookList.txt", "w") as outfile:
        for book in bookList:
            outfile.write(",".join(book) + "\n")


if __name__ == "__main__":
    main()
