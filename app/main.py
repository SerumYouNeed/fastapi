from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# To see this use: uvicorn main(to jest nazwa pliku):app(to jest nazwa instancji z linii 3)
# Path operation / rout 
@app.get("/") # W nawiasie masz url
def root(): # nazwij to opisowo
    # tu jest to co zwraca funkcja userowi. ten słownik z automatu zamieni na json
    return {"message": "Hello World"}