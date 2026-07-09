from fastapi import FastAPI
from .db  import Base, engine
from .routers import router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Task API",
    version="1.0"
)
app.include_router(router)