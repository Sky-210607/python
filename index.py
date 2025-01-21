import getpass
import json


try:
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
except FileNotFoundError:
    user_data = {'admins': [], 'users': []}

books = [
    {"title": "Song of Achilles", "author": "Madeline Miller", "isbn": "0-547-93850-5", "status": "Available"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "1-84159-413-5", "status": "Available"},
    {"title": "Little Women", "author": "Louisa May Alcott", "isbn": "0-06078-202-8", "status": "Available"}
]

members = []

def signup(role):
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return

    if role == 'admin':
        user_data['admins'].append({'username': username, 'password': password})
    elif role == 'user':
        user_data['users'].append({'username': username, 'password': password})

    with open('user_data.json', 'w') as f:
        json.dump(user_data, f)

    print("Signup successful!")

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    for user in user_data['admins']:
        if user['username'] == username and user['password'] == password:
            return 'admin'
    for user in user_data['users']:
        if user['username'] == username and user['password'] == password:
            return 'user'

    print("Invalid username or password")
    return None

def add_book(title, author, isbn):
    book = {"title": title, "author": author, "isbn": isbn, "status": "Available"}
    books.append(book)
    print("Book added successfully!")

def view_all_books():
    if not books:
        print("No books in the library.")
    else:
        print("List of Books:")
        for i, book in enumerate(books, 1):
            print(f"{i}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {book['status']}")

def search_book(query):
    found_books = []
    for book in books:
        if query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or query.lower() in book['isbn'].lower():
            found_books.append(book)
    if found_books:
        print("Books found:")
        for i, book in enumerate(found_books, 1):
            print(f"{i}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {book['status']}")
    else:
        print("No books found.")

def remove_book(book_title):
    for book in books:
        if book['title'] == book_title:
            books.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def issue_book(isbn):
    for book in books:
        if book['isbn'] == isbn:
            if book['status'] == 'Available':
                book['status'] = 'Issued'
                print("Book issued successfully!")
            else:
                print("Book is not available.")
            return
    print("Book not found.")

def return_book(isbn):
    for book in books:
        if book['isbn'] == isbn:
            if book['status'] == 'Issued':
                book['status'] = 'Available'
                print("Book returned successfully!")
            else:
                print("Book is already available.")
            return
    print("Book not found.")

def add_member(name, id):
    member = {"name": name, "id": id, "status": "Available"}
    members.append(member)
    print("Member added successfully!")

def view_all_members():
    if not members:
        print("No members to show")
    else:
        print("All Members:")
        for i, member in enumerate(members, 1):
            print(f"{i}. Name: {member['name']}, ID: {member['id']}, Status: {member['status']}")

def member_leave(id):
    for member in members:
        if member['id'] == id:
            if member['status'] == 'Available':
                member['status'] = 'On leave'
                print("Member's leave approved successfully!")
            else:
                print("Member is not available.")
            return
    print("Member not found.")

def remove_member(member_id):
    for member in members:
        if member['id'] == member_id:
            members.remove(member)
            print("Member removed successfully!")
            return
    print("Member not found.")

def search_member(query):
    found_members = []
    for member in members:
        if query.lower() in member['name'].lower() or query.lower() in member['id'].lower() or query.lower() in member['status'].lower():
            found_members.append(member)
    if found_members:
        print("Members found:")
        for i, member in enumerate(found_members, 1):
            print(f"{i}. Name: {member['name']}, ID: {member['id']}, Status: {member['status']}")
    else:
        print("No member found.")

while True:
    print("1. Signup")
    print("2. Login")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 2:
        role = login()
        if role is None:
            continue

        while True:
            if role == "admin":
                print("\nAdmin Panel")
                print("WELCOME TO LIBRARY MANAGEMENT SYSTEM")
                print("1. Add Book")
                print("2. View All Books")
                print("3. Search Book")
                print("4. Remove Book")
                print("5. Add Member")
                print("6. View All Members")
                print("7. Search Members")
                print("8. Approve Member's leave")
                print("9. Remove Member")
                print("10. Logout")
                print("0. Exit")

                choice = int(input("Enter your choice: "))
                if choice==1:
                    title = input("Enter book title: ")
                    author = input("Enter author name: ")
                    isbn = input("Enter ISBN: ")
                    add_book(title, author, isbn)
                elif choice==2:
                    view_all_books()
                elif choice==3:
                    query = input("Enter book title: ")
                    search_book(query)
                elif choice==4:
                    book_title = input("Enter the title of the book to remove: ")
                    remove_book(book_title)
                elif choice==5:
                    name= input("Enter the name of the member to be added:")
                    id= input("Enter ID of the new member:")
                    add_member(name,id)
                elif choice==6:
                    view_all_members()
                elif choice==7:
                    query = input("Enter member's name: ")
                    search_member(query)
                elif choice==8:
                    id = input("Enter ID of the member whose leave to be approved: ")
                    member_leave(id)
                elif choice==9:
                    member_id = input("Enter the ID of the member to remove: ")
                    remove_member(member_id)
                elif choice==10:
                    print("Logging out..")
                    break
                    
                    
                                  
                    
            elif role == "user":
                print("\nUser Panel")
                print("WELCOME TO LIBRARY MANAGEMENT SYSTEM")
                print("1. View All Books")
                print("2. Search Book")
                print("3. Issue Book")
                print("4. Return Book")
                print("5. View Members")
                print("6. Logout")
                print("0. Exit")

                choice = int(input("Enter your choice: "))
                if choice==1:
                    view_all_books()
                elif choice==2:
                     query = input("Enter book title: ")
                     search_book(query)
                elif choice==3:
                    isbn = input("Enter ISBN of the book to issue: ")
                    issue_book(isbn)
                elif choice==4:
                    isbn = input("Enter ISBN of the book to return: ")
                    return_book(isbn)
                elif choice==5:
                    view_all_members()
                elif choice==6:
                    print("Logging out")
                    break
                
                     

            if choice == 0:
                print("Exiting...")
                break
            elif choice not in range(1, 8):
                print("Invalid choice. Please try again.")

    elif choice == 1:
        print("1. Admin Signup")
        print("2. User Signup")
        signup_choice = int(input("Enter your choice: "))
        if signup_choice == 1:
            signup('admin')
        elif signup_choice == 2:
            signup('user')
        else:
            print("Invalid choice.")

    elif choice == 0:
        print("Exiting Library Management System...")
        break
    else:
        print("Invalid choice. Please try again.")
