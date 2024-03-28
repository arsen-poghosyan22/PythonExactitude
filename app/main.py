from fastapi import FastAPI
from resources.search import searching_router

def main():
    app = FastAPI()
    app.include_router(searching_router)

    return app

app = main()