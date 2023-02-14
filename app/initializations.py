import json
from sqlalchemy.orm import Session
from schemas import Pipeline
from dependencies import get_db
from db.models import Base, Pipeline as dbPipeline, Stage as dbStage, Relation as dbRelation
import crud


def add_pipelines(db: Session = next(get_db())):
    with open("pipelines.json") as json_file:
        pipelines = json.load(json_file)
        pipelines = pipelines.get("pipelines")
        pipelines = [Pipeline(**x) for x in pipelines]
        for pipeline in pipelines:
            if not crud.get_pipeline_by_name(db=db, name=pipeline.name):
                db_pipeline = dbPipeline(name=pipeline.name)
                db.add(db_pipeline)
            for stage in pipeline.stages:
                if not crud.get_stage_by_name(db=db, name=stage.name):
                    db_stage = dbStage(name=stage.name)
                    db.add(db_stage)
                    db.commit()
                    db.add(dbRelation(pipeline_id=db_pipeline.id, stage_id=db_stage.id))
        db.commit()
