import csv

CONTACTS_FILE = "contacts.csv"

# Function to load contacts from CSV
def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)
    except FileNotFoundError:
        pass
    return contacts

# Function to save contacts to CSV
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contacts.append([name, phone, email])
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to display all contacts
def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts List:")
        print("-" * 40)
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
        print("-" * 40)

# Function to search for a contact
def search_contact():
    query = input("Enter name or phone to search: ").lower()
    results = [c for c in contacts if query in c[0].lower() or query in c[1]]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
    else:
        print("No matching contacts found.")

# Function to update a contact
def update_contact():
    view_contacts()
    try:
        index = int(input("Enter the line number to update: ")) - 1
        if 0 <= index < len(contacts):
            name = input("Enter New Name: ") or contacts[index][0]
            phone = input("Enter New Phone: ") or contacts[index][1]
            email = input("Enter New Email: ") or contacts[index][2]
            contacts[index] = [name, phone, email]
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number!")
    except ValueError:
        print("Please enter a valid number!")

# Function to delete a contact
def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted Contact: {deleted[0]}")
        else:
            print("Invalid contact number!")
    except ValueError:
        print("Please enter a valid number!")

# Load contacts initially
contacts = load_contacts()

# Main Menu
while True:
    print("\nContact Manager Options:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
