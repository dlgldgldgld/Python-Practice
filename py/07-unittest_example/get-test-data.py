from booksearch import get_books
book = get_books(q='python')[0]
book.save_thumbnails('test/data')