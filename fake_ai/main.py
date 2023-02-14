import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas import PostImage
from services.ai import AI
import crud
from db.session import engine
from db.models import Base


Base.metadata.create_all(bind=engine)


app = FastAPI(
    root_path=os.getenv("FAKE_AI_ROOT_PATH"),
    title=os.getenv("FAKE_AI_TITLE"),
    description=os.getenv("FAKE_AI_DESCRIPTION"),
    version=os.getenv("FAKE_AI_VERSION")
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "fake_ai"}


@app.get("/healthcheck")
async def healthcheck():
    return {"message": "fake_ai"}


@app.post("/detect_auto")
async def detect_auto_on_image(image: PostImage,
                               db: Session = Depends(get_db)):
    if not crud.get_db_image_by_image_string(db=db, image_string=image.image_string):
        detecting = AI(image.image_string).detect_auto()
        if detecting:
            crud.create_filled_image(db=db, image=detecting)
        else:
            crud.create_empty_image(db=db, image_string=image.image_string)
    return {"message": "success"}
