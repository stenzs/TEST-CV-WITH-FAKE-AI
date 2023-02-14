from sqlalchemy import Column, String, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from db.session import Base


class Pipeline(Base):
    __tablename__ = "pipelines"
    __table_args__ = {"schema": "public"}
    id = Column("id", BigInteger, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)
    name = Column("name", String, unique=True)


class Stage(Base):
    __tablename__ = "stages"
    __table_args__ = {"schema": "public"}
    id = Column("id", BigInteger, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)
    name = Column("name", String, unique=True)


class Relation(Base):
    __tablename__ = "relation_pipeline_to_stages"
    __table_args__ = {"schema": "public"}
    id = Column("id", BigInteger, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)
    pipeline_id: Mapped[int] = mapped_column(ForeignKey("public.pipelines.id"))
    stage_id: Mapped[int] = mapped_column(ForeignKey("public.stages.id"))
