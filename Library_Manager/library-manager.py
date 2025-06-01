import json

# Constants
LIBRARY_FILE = "library.json"

def load_library():
    """Load library data from file"""
    try:
        with open(LIBRARY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save library data to file"""
    with open(LIBRARY_FILE, 'w') as f:
        json.dump(library, f)

def get_input(prompt, required=True):
    """Get validated user input"""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("This field is required!")

def add_book(library):
    """Add a new book to the library"""
    print("\nAdd New Book")
    book = {
        "title": get_input("Title: "),
        "author": get_input("Author: "),
        "year": get_input("Year: "),
        "genre": get_input("Genre: "),
        "read": get_input("Read? (y/n): ").lower() == 'y'
    }
    library.append(book)
    save_library(library)
    print(f"'{book['title']}' added successfully!")

def remove_book(library):
    """Remove a book from the library"""
    title = get_input("\nEnter title to remove: ")
    for book in library[:]:
        if book['title'].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print(f"Removed '{book['title']}'")
            return
    print("Book not found!")

def search_books(library):
    """Search books by title or author"""
    search_type = get_input("\nSearch by (title/author): ").lower()
    if search_type not in ['title', 'author']:
        print("Invalid search type!")
        return
    
    term = get_input(f"Enter {search_type}: ").lower()
    found = [b for b in library if term in b[search_type].lower()]
    
    if found:
        print("\nFound Books:")
        for book in found:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No books found!")

def show_stats(library):
    """Display library statistics"""
    total = len(library)
    read = sum(1 for book in library if book['read'])
    percent = (read/total)*100 if total > 0 else 0
    print(f"\nTotal Books: {total}")
    print(f"Read: {read} ({percent:.1f}%)")

def show_all(library):
    """Display all books in the library"""
    print("\nYour Library:")
    if not library:
        print("No books yet!")
        return
    
    for i, book in enumerate(library, 1):
        status = "Read" if book['read'] else "Unread"
        print(f"{i}. {book['title']} by {book['author']}")

def main():
    """Main program loop"""
    library = load_library()
    
    while True:
        print("\nMENU")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. View All Books")
        print("5. Statistics")
        print("6. Exit")
        
        choice = input("Choose (1-6): ")
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            show_all(library)
        elif choice == '5':
            show_stats(library)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    print("Personal Library Manager")
    main()