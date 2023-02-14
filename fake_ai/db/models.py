from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from db.session import Base


class Image(Base):
    __tablename__ = "images"
    __table_args__ = {"schema": "public"}
    uuid = Column("uuid", UUID(as_uuid=True), index=True, primary_key=True, unique=True, nullable=False)
    image_string = Column("image_string", String, nullable=False)
    top_left_x = Column("top_left_x", Integer)
    top_left_y = Column("top_left_y", Integer)
    w = Column("w", Integer)
    h = Column("h", Integer)
    conf = Column("conf", Float)
    label = Column("label", Integer)
