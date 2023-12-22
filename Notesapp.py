import os

def display_menu():
    print("Simple Notes App")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

def add_note():
    note = input("Enter your note: ")
    notes.append(note)
    print("Note added successfully!")

def view_notes():
    if not notes:
        print("No notes available.")
    else:
        print("Your Notes:")
        for idx, note in enumerate(notes, start=1):
            print(f"{idx}. {note}")

# Initialize an empty list to store notes
notes = []

while True:
    display_menu()

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Exiting the Notes App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    input("Press Enter to continue...")  # Pause to allow the user to read the output
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen for better visibility
