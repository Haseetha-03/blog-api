# Blog API

A RESTful API built using FastAPI and PostgreSQL to manage authors and their posts.  
This project demonstrates a one-to-many relationship, cascade delete, and efficient database queries.

---

## 🚀 Features

- Create and delete authors
- Create and retrieve posts
- One-to-many relationship (Author → Posts)
- Cascade delete (deleting an author removes their posts)
- Nested endpoint to retrieve posts by author
- Swagger API documentation

---

## 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ORM

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd blog_api
