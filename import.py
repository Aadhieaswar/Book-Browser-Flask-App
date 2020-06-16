import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def create():
    db.create_all()

def main():
    b = open("books.csv")
    reader = csv.reader(b)
    for isbn, title, author, year in reader:
        books = Book(isbn=isbn, title=title, author=author, year=year)
        db.session.add(books)
        print(f"Added book with ISBN {isbn}, title {title}, author {author} on the year {year}.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        create(), main()
