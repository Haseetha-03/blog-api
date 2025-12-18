from fastapi import FastAPI
from app.database import Base, engine
from app.routes import author_routes, post_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API")

app.include_router(author_routes.router)
app.include_router(post_routes.router)
