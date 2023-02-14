import os
from fastapi import FastAPI, UploadFile, BackgroundTasks, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dependencies import get_db
import crud
from services.run_pipeline import run_pipeline
from initializations import add_pipelines
from db.models import Base
from db.session import engine


Base.metadata.create_all(bind=engine)
add_pipelines()


app = FastAPI(
    root_path=os.getenv("APP_ROOT_PATH"),
    title=os.getenv("APP_TITLE"),
    description=os.getenv("APP_DESCRIPTION"),
    version=os.getenv("APP_VERSION")
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
    return {"message": "hello"}


@app.post("/process_image")
async def process_image(pipeline_id: int,
                        file: UploadFile,
                        background_tasks: BackgroundTasks,
                        db: Session = Depends(get_db)):
    pipeline = crud.get_pipeline_by_id(db=db, pipeline_id=pipeline_id)
    if not pipeline:
        return {"message": "no pipeline with this id, try 1"}

    background_tasks.add_task(run_pipeline, pipeline, file)
    return {"message": "success"}
