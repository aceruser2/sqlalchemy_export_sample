# coding: utf-8
from sqlalchemy import Column, MetaData, String, Table

metadata = MetaData()


t_newtable = Table(
    'newtable', metadata,
    Column('column1', String, comment='隨便')
)
