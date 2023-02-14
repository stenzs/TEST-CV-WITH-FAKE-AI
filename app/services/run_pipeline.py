from services import cv
from services import detect_auto_frame
import crud
from dependencies import get_db


def run_pipeline(pipeline, file):
    stages = crud.get_stages_by_pipeline_id(db=next(get_db()), pipeline_id=pipeline.id)
    stages = [x.name for x in stages]
    image_string = None
    if "photo_processing" in stages:
        image_string = cv.transform_image(file)
    if "detect_auto_frame" in stages and image_string:
        detect_auto_frame.request_detecting(image_string)
