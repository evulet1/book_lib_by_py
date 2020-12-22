'''
Concered with storing and retrieving books from list
'''

books = []

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})

def get_all_books():
    return books

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name] # add each book to new list if book['name'] != namecommit


    for book in books:
        if book['name'] == name:
            book.remove(book)

