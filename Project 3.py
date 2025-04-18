# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hj316q-i-tA1-zRovlxF4baZaJM8aqHH
"""

# Personal Library Manager

library = []

def add_book():
    title = input("Book Title: ")
    author = input("Author: ")
    year = input("Year: ")
    read = input("Have you read it? (yes/no): ").lower() == "yes"
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "read": read
    })
    print(f"'{title}' added to your library.")

def view_books():
    if not library:
        print("Your library is empty.")
        return
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {status}")

def mark_as_read():
    view_books()
    try:
        choice = int(input("Enter the number of the book you read: ")) - 1
        if 0 <= choice < len(library):
            library[choice]["read"] = True
            print(f"Marked '{library[choice]['title']}' as read.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def remove_book():
    view_books()
    try:
        choice = int(input("Enter the number of the book to remove: ")) - 1
        if 0 <= choice < len(library):
            removed = library.pop(choice)
            print(f"Removed '{removed['title']}' from your library.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    while True:
        print("\nPersonal Library Manager")
        print("1. Add Book")
        print("2. View Books")
        print("3. Mark Book as Read")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            mark_as_read()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()