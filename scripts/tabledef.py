# -*- coding: utf-8 -*-

import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'sqlite:///accounts.db'

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(SQLALCHEMY_DATABASE_URI)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    query = Column(String(250), unique=True)
 

    def __repr__(self):
        return '<User %r>' % self.query


engine = db_connect()  # Connect to database
Base.metadata.create_all(engine)  # Create models
