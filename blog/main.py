from fastapi import FastAPI
from typing import Optional
from . import schemas, models
from .database import engine

import uvicorn


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post('/blog')
def create(blog: schemas.Blog):
    return blog
