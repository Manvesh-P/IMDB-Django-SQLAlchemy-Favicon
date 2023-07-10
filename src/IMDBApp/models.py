from django.db import models
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Float,
                        ARRAY)
from sqlalchemy.ext.declarative import declarative_base
# Create your models here.

Base = declarative_base()

# class IMDB(Base):
#     __tablename__ = 'imdb_info'

#     _id = Column(String, primary_key=True)
#     popularity = Column(Float)
#     director = Column(String)
#     genre = Column(ARRAY(String))
#     imdb_score = Column(Float)
#     name = Column(String)

# class IMDB(Base):
#     __tablename__ = 'imdb_info_1'

#     _id = Column(String, primary_key=True)
#     popularity = Column(Float)
#     director = Column(String)
#     genre = Column(ARRAY(String))
#     imdb_score = Column(Float)
#     name = Column(String)

class IMDB(Base):
    __tablename__ = 'imdb_info_two'

    _id = Column(String, primary_key=True)
    popularity = Column(Float)
    director = Column(String)
    genre = Column(ARRAY(String))
    imdb_score = Column(Float)
    name = Column(String)




