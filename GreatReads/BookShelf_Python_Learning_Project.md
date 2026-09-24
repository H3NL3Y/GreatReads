# BookShelf — Python Learning Project

## Overall Goal

Build a personal Goodreads-style book-tracking application while using the project to progressively develop your Python and software-development skills.

The project should start as a simple command-line application and eventually become a full web application with a database, API, recommendations, testing and deployment.

> **Project principle:** Use AI to explain, debug and review your code — but write the first version yourself.

---

# Level 1 — Python Fundamentals

### Goal

Build a command-line book tracker.

Do **not** use Flask yet.

The application should allow you to:

1. Add a book
2. List books
3. Search books
4. Add a rating
5. Change reading status
6. Remove a book
7. Display statistics

Example:

```text
=== My Books ===

1. The Hobbit
   J.R.R. Tolkien
   ★★★★★
   Status: Read

2. Dune
   Frank Herbert
   ★★★★☆
   Status: Reading
```

### Skills to develop

- Variables
- Strings
- Lists
- Dictionaries
- Tuples
- `if / elif / else`
- `for` and `while`
- Functions
- Input validation
- Exception handling
- Modules
- Reading and writing files

### Project structure

Do not create one enormous Python file.

Aim for something like:

```text
goodreads_clone/
│
├── main.py
├── books.py
├── users.py
├── library.py
└── data/
    └── books.json
```

This stage should teach you how to structure a real application.

---

# Level 2 — Data & Persistence

Make the application remember things when it closes.

Start with:

```text
JSON
```

Then move to:

```text
SQLite
```

SQLite should be a major milestone.

### Suggested database structure

```text
users
---------
id
username
email
password_hash
```

```text
books
---------
id
title
isbn
publication_year
description
```

```text
user_books
---------
user_id
book_id
status
date_started
date_finished
```

You will eventually want tables for:

- Users
- Books
- Authors
- User books
- Reviews
- Ratings

### Skills to develop

- JSON
- File handling
- SQL
- SQLite
- CRUD
- Database relationships
- Primary keys
- Foreign keys
- SQL joins

---

# Level 3 — Object-Oriented Python

Refactor parts of the application using classes.

For example:

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
```

Potential classes:

```text
Book
User
Review
Library
```

Do not turn everything into a class simply because you can.

The goal is to understand:

- Classes
- Objects
- Methods
- `__init__`
- Properties
- Inheritance
- Composition
- Dataclasses

Specifically practise:

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    isbn: str
```

---

# Level 4 — Turn It Into a Web Application

Once the core application works, turn it into a web application.

Use:

**Python + Flask**

The architecture becomes:

```text
Browser
   ↓
Flask
   ↓
Python
   ↓
SQLite
```

### Pages

Build pages for:

```text
/
├── Home
├── Books
├── Book details
├── Search
├── My Library
├── Add review
├── Profile
└── Login
```

Example:

```text
http://localhost:5000/books/123
```

Could display:

> **The Hobbit**  
> J.R.R. Tolkien  
> Published: 1937  
>
> ★★★★★  
>
> [Want to Read] [Currently Reading] [Finished]

### Skills to develop

- Flask
- Routing
- Templates
- Jinja2
- HTML
- Forms
- GET / POST
- Sessions
- Cookies
- Authentication
- HTTP fundamentals

---

# Level 5 — Build a Proper API

Once the web application works, build an API for it.

Example endpoints:

```http
GET /api/books
GET /api/books/123
POST /api/books
POST /api/books/123/reviews
```

Example response:

```json
{
    "id": 123,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "rating": 4.8
}
```

Possible technologies:

- Flask + Flask-RESTful
- FastAPI

A useful longer-term goal is to learn **FastAPI** after Flask so that you gain experience with a modern Python API framework.

### Skills to develop

- REST
- API design
- JSON
- HTTP status codes
- Request/response handling
- API validation
- Authentication
- API documentation

---

# Level 6 — External APIs

Stop manually entering every book.

Connect your application to an external book API.

Example workflow:

```text
User searches:

"Dune"
      ↓
Your Python application
      ↓
Book API
      ↓
Dune
Frank Herbert
1965
ISBN...
Cover...
Description...
```

Then:

> **Add to my library**

stores the book in your database.

### Skills to develop

- HTTP requests
- REST APIs
- JSON responses
- API authentication
- Query parameters
- Error handling
- Rate limiting
- Environment variables

---

# Level 7 — Recommendations

Build your own mini recommendation engine.

Do not start with AI or machine learning.

Start with rules based on:

- Genre
- Author
- Tags
- Ratings
- Books users have read together
- Average rating

For example:

```text
Users who liked Dune
        ↓
also liked
        ↓
Foundation
Hyperion
The Left Hand of Darkness
```

Eventually explore:

```text
similarity(book A, book B)
```

and then:

**Collaborative filtering**

This stage can introduce you to data science and machine-learning concepts.

---

# Level 8 — Make It Production Quality

Take the application and make it something you could genuinely deploy.

## Testing

Create:

```text
tests/
├── test_books.py
├── test_users.py
├── test_library.py
└── test_api.py
```

Learn:

```text
pytest
```

## Type Hints

Move from:

```python
def get_book(id):
```

towards:

```python
def get_book(book_id: int) -> Book | None:
```

## Code Quality

Explore:

```text
ruff
black
mypy
```

Learn:

- Linting
- Formatting
- Static type checking
- Docstrings
- Maintainable code

## Git

Use Git throughout the project.

Example branches:

```text
main
│
├── feature/user-auth
├── feature/book-search
├── feature/reviews
└── feature/recommendations
```

Make meaningful commits:

```text
Add book model
Implement SQLite persistence
Add user authentication
Create book search endpoint
Add review system
```

---

# Final Project — BookShelf

The final goal is a self-hosted Goodreads-style application.

## Architecture

```text
                    ┌──────────────┐
                    │   Browser    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Flask     │
                    │  Web Server  │
                    └──────┬───────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       ┌──────────────┐          ┌──────────────┐
       │    SQLite    │          │  Book API    │
       │   Database   │          │              │
       └──────────────┘          └──────────────┘
```

## Final Feature Set

```text
BookShelf
│
├── Authentication
├── User profiles
├── Book search
├── Personal library
├── Reading status
├── Ratings
├── Reviews
├── Reading statistics
├── Friends/following
├── Recommendations
├── REST API
├── Tests
└── Docker deployment
```

---

# Learning Goals

The most important outcome is **not simply building Goodreads**.

Measure success by the Python and software-development skills you acquire.

| Stage | Main Skill |
|---|---|
| 1 | Core Python |
| 2 | Files & databases |
| 3 | Object-oriented Python |
| 4 | Flask / web development |
| 5 | REST APIs |
| 6 | External APIs |
| 7 | Algorithms / data |
| 8 | Testing / production Python |

---

# Rules for the Project

## 1. Build incrementally

Do not try to build the entire application at once.

Each level should produce a working application.

## 2. Avoid unnecessary complexity

Only introduce a new technology when the project has a reason to need it.

## 3. Use AI as a tutor

Good uses of AI:

- Explain an error
- Explain unfamiliar Python
- Review your code
- Suggest improvements
- Explain architecture
- Help you understand documentation
- Give you hints when you're stuck
- Write tests after you understand the underlying code

Avoid:

- Asking AI to build the whole project
- Copying large amounts of code without understanding it
- Using libraries without understanding what problem they solve

## 4. Keep everything in Git

Commit regularly and use meaningful commit messages.

## 5. Refactor as you learn

Your early code does not need to be perfect.

Part of the project is returning to older code and improving it as your skills develop.

---

# Definition of Done

The project is successful when you can explain, without relying on AI:

- How your Python application is structured
- How your classes work
- How your database is structured
- How SQL queries interact with Python
- How Flask handles a request
- How a web form reaches your Python code
- How authentication works
- How your API works
- How your application communicates with an external API
- How your tests work
- How you would deploy the application

The ultimate goal is not:

> "I built a Goodreads clone."

It is:

> **"I understand enough Python to design, build, debug, test and deploy a real application."**
