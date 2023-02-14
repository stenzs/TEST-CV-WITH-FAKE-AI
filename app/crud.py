from sqlalchemy.orm import Session
from db.models import Pipeline as dbPipeline, Stage as dbStage, Relation as dbRelation


def get_pipeline_by_id(db: Session, pipeline_id: int):
    db_pipeline = db.query(dbPipeline).filter(dbPipeline.id == pipeline_id).first()
    return db_pipeline


def get_pipeline_by_name(db: Session, name: str):
    db_pipeline = db.query(dbPipeline).filter(dbPipeline.name == name).first()
    return db_pipeline


def get_stage_by_name(db: Session, name: str):
    db_stage = db.query(dbStage).filter(dbStage.name == name).first()
    return db_stage


def get_stages_by_pipeline_id(db: Session, pipeline_id: int):
    db_stages_ids = db.query(dbRelation).filter(dbRelation.pipeline_id == pipeline_id).all()
    db_stages = db.query(dbStage).filter(dbStage.id.in_((x.id for x in db_stages_ids))).all()
    return db_stages
