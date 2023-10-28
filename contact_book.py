class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword in contact.name or keyword in contact.phone_number]
        for contact in results:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, old_contact, new_contact):
        index = self.contacts.index(old_contact)
        self.contacts[index] = new_contact
        print("Contact updated successfully.")

    def delete_contact(self, contact):
        self.contacts.remove(contact)
        print("Contact deleted successfully.")

# Example usage: (modify and complete the logic for the update and delete options)
contact_book = ContactBook()
while True:
    print("""
    ---------------------------------------
    |            Contact Book             |
    ---------------------------------------
    | Options:                            |
    | 1. Add Contact                      |
    | 2. View Contacts                    |
    | 3. Search Contact                   |
    | 4. Update Contact                   |
    | 5. Delete Contact                   |
    | 6. Exit                             |
    ---------------------------------------
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact_book.add_contact(name, phone_number, email, address)

    elif choice == "2":
        contact_book.view_contacts()

    elif choice == "3":
        keyword = input("Enter name or phone number to search: ")
        contact_book.search_contact(keyword)

    elif choice == "4":
        # Update logic here
        old_contact_name = input("Enter the name of the contact to update: ")
        for contact in contact_book.contacts:
            if contact.name == old_contact_name:
                new_name = input("Enter new name: ")
                new_phone_number = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                new_contact = Contact(new_name, new_phone_number, new_email, new_address)
                contact_book.update_contact(contact, new_contact)
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        # Delete logic here
        contact_name = input("Enter the name of the contact to delete: ")
        for contact in contact_book.contacts:
            if contact.name == contact_name:
                contact_book.delete_contact(contact)
                break
        else:
            print("Contact not found.")

    elif choice == "6":
        break

    else:
        print("Invalid choice. Please select a valid option.")
