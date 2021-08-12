from fastapi import FastAPI

app = FastAPI()


# @app path operation decorator
# .get() path operator
# ('/') path
# funciton is called path operator function
@app.get('/')
def index():
    return {'data': {'name': 'Deepankar'}}


@app.get('/blog/unpublished')
def show():
    # fetch blog which are unpublished
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


@app.get('/about')
def about():
    return {'data': 'about page'}
