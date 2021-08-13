from fastapi import FastAPI
from typing import Optional
from . import schemas

import uvicorn


app = FastAPI()


@app.post('/blog')
def create(blog: schemas.Blog):
    return blog
