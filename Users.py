from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///mymusic.db', echo=True)
Base = declarative_base()

########################################################################
class Users(Base):
    """"""
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, name):
        """"""
        self.name = name

Base.metadata.create_all(engine)