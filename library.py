from datetime import datetime, timedelta
# ========== DATA ==========
books = {
"B001": {"title": "Harry Potter", "author": "J.K. Rowling", "available": False},
"B002": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
"B003": {"title": "1984", "author": "George Orwell", "available": True},
"B004": {"title": "The Little Prince", "author": "Antoine de Saint", "available": True},
"B005": {"title": "Pride and Prejudice", "author": "Jane Austen", "available": False},
}

readers = {
"R001": {"name": "David", "books_borrowed": ["B002"]},
"R002": {"name": "Yael", "books_borrowed": ["B005"]},
"R003": {"name": "Noam", "books_borrowed": []},
"R004": {"name": "Shira", "books_borrowed": []},
}

loans = {
"B002": {"reader_id": "R001", "due_date": "2024-02-15"},
"B005": {"reader_id": "R002", "due_date": "2024-02-10"},
}
# ========== LOAN FUNCTIONS ==========

def borrow_book(book_id, reader_id):
    if book_id not in books:
        print("Book not found")
        return False
    if not books[book_id]["available"]:
        print("Book not available")
        return False
    books[book_id]["available"] = False
    readers[reader_id]["books_borrowed"].append(book_id)
    due_date = datetime.now() + timedelta(days=14)
    loans[book_id] = {
        "reader_id": reader_id,
        "due_date": due_date.strftime("%Y-%m-%d")
    }
    print(f"Book borrowed successfully. Due date: {loans[book_id]['due_date']}")
    return True

def return_book(book_id):
    if book_id not in loans:
        print("Book is not on loan")
        return False
    reader_id = loans[book_id]["reader_id"]
    books[book_id]["available"] = True
    readers[reader_id]["books_borrowed"].remove(book_id)
    del loans[book_id]
    print("Book returned successfully")
    return True

# extend_loan(book_id, days)
def extend_loan(book_id, days):
    if book_id not in loans:
        print("Book is not on loan")
        return False
    current_due = datetime.strptime(loans[book_id]["due_date"], "%Y-%m-%d")
    new_due = current_due + timedelta(days=days)
    loans[book_id]["due_date"] = new_due.strftime("%Y-%m-%d")

    print(f"Loan extended. New due date: {loans[book_id]['due_date']}")
    return True

# ========== REPORT FUNCTIONS ==========
# TODO: search_book(title)
# TODO: get_available_books()
# TODO: get_overdue_loans()
# ========== MAIN ==========
if __name__ == "__main__":
    print("Library System Ready")
    print("Data loaded: 5 books, 4 readers")
    print("Loan functions ready")

