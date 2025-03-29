from fastapi import FastAPI
from models.books import BookResponse

app = FastAPI()


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
    }


@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {"author_id": author_id, "name": "Ernest Hermingway"}


@app.get("/allbooks")
async def read_all_books(id: int) -> list[BookResponse]:
    return [
        {"id": id, "title": "1984", "author": "George Orwell"},
        {"id": id, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    ]
