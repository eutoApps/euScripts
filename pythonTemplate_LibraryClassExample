'''Template Python class containing if-else, while loop, for loop,
initialization, class variables, functions, lists,
dictionary, file input and output.

by eutoApps / Eric Utomo
November 2024
'''

class Library:
    # Class variable; all Library objects will have these same 4 books
    available_books = ["Super Important Book 1", "Super Important Book 2", "Super Important Book 3", "Super Important Book 4"]
    
    def __init__(self):
        # Instance variables
        self.checked_out_books = {}  # Dictionary key is the user, value is a list of their checked out books
        self.activity_log = []  # List to store library activities; read and write with a file
    
    # Function to display available books
    def display_books(self):
        print("Available Books:")
        for book in Library.available_books:
            print(f"- {book}")
    
    def check_out(self, user, book_name):
        if book_name in Library.available_books:
            Library.available_books.remove(book_name)
            if user in self.checked_out_books:
                self.checked_out_books[user].append(book_name)
            else:
                self.checked_out_books[user] = [book_name]
            self.activity_log.append(f"{user} checked out {book_name}")
            print(f"{book_name} has been checked out by {user}.")
        else:
            print(f"Sorry, {book_name} is not available.")

    def return_book(self, user, book_name):
        if user in self.checked_out_books and book_name in self.checked_out_books[user]:
            self.checked_out_books[user].remove(book_name)
            Library.available_books.append(book_name)
            self.activity_log.append(f"{user} returned {book_name}")
            print(f"{book_name} has been returned by {user}.")
            if not self.checked_out_books[user]:
                del self.checked_out_books[user]  # Clean up if user has no more books
        else:
            print(f"{user} has not checked out {book_name}.")
    
    #Log activities to a file
    def save_log_to_file(self, file_name="library_log.txt"):
        with open(file_name, "w") as file:
            for activity in self.activity_log:
                file.write(activity + "\n")
        print(f"Activity log saved to {file_name}.")
    
    #Load log from a file
    def load_log_from_file(self, file_name="library_log.txt"):
        try:
            with open(file_name, "r") as file:
                self.activity_log = [line.strip() for line in file.readlines()]
            print(f"Activity log loaded from {file_name}.")
        except FileNotFoundError:
            print(f"{file_name} does not exist.")
    
    #Simulated library day
    def run_library_day(self):
        print("Welcome to the Library!")
        while True:
            print("\nMenu:")
            print("1. Display Books")
            print("2. Check Out Book")
            print("3. Return Book")
            print("4. Save Log")
            print("5. Load Log")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_books()
            elif choice == "2":
                user = input("Enter your name: ")
                book_name = input("Enter the book name: ")
                self.check_out(user, book_name)
            elif choice == "3":
                user = input("Enter your name: ")
                book_name = input("Enter the book name: ")
                self.return_book(user, book_name)
            elif choice == "4":
                self.save_log_to_file()
            elif choice == "5":
                self.load_log_from_file()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Example use
if __name__ == "__main__":
    library = Library()
    library.run_library_day()
