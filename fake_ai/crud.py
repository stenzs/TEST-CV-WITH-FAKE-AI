import uuid
from sqlalchemy.orm import Session
from db.models import Image as dbImage
from schemas import Image


def create_filled_image(db: Session, image: Image):
    db_image = dbImage(
        uuid=uuid.uuid4(),
        image_string=image.image_string,
        top_left_x=image.top_left_x,
        top_left_y=image.top_left_y,
        w=image.w,
        h=image.h,
        conf=image.conf,
        label=image.label,
    )
    db.add(db_image)
    db.commit()
    return True


def create_empty_image(db: Session, image_string: str):
    db_image = dbImage(
        uuid=uuid.uuid4(),
        image_string=image_string,
        top_left_x=None,
        top_left_y=None,
        w=None,
        h=None,
        conf=None,
        label=0,
    )
    db.add(db_image)
    db.commit()
    return True


def get_db_image_by_image_string(db: Session, image_string: str):
    db_image = db.query(dbImage).filter(dbImage.image_string == image_string).first()
    return db_image
