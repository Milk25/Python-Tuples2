def add_book(library, title, author):
    new_book = (title, author)
    
    if new_book in library:
        print("This book already exists in the library.")
    else:
        library.append(new_book)
        print("Book added successfully.")

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Example usage
add_book(library, "1984", "George Orwell")  # Trying to add a duplicate book
add_book(library, "Animal Farm", "George Orwell")  # Adding a new book
print(library)