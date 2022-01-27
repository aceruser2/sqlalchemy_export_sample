# coding: utf-8
from sqlalchemy import Column, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_item = Table(
    'item', metadata,
    Column('id', String),
    Column('item', String),
    Column('price', String)
)


class Order(Base):
    __tablename__ = 'order'

    id = Column(String, primary_key=True)
    item_id = Column(String)
    blance = Column(String)
    user_id = Column(String)


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
