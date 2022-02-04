# coding: utf-8
from sqlalchemy import Boolean, Column, Date, ForeignKey, JSON, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BathroomLog(Base):
    __tablename__ = 'bathroom_log'

    id = Column(UUID, primary_key=True, unique=True, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID, nullable=False)
    room_id = Column(UUID, nullable=False)
    is_in = Column(Boolean, nullable=False)
    create_dt = Column(Date, nullable=False)
    update_dt = Column(Date, nullable=False)


class ErrLog(Base):
    __tablename__ = 'err_log'

    id = Column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    err_msg = Column(JSON, nullable=False)
    create_dt = Column(Date, nullable=False)
    update_dt = Column(Date, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, server_default=text("gen_random_uuid()"), comment='uuid填入時不得為空pk')
    name = Column(String, nullable=False, comment='姓名')
    job_id = Column(String, nullable=False, comment='工號')
    create_dt = Column(Date, nullable=False, comment='創建時間')
    update_dt = Column(Date, nullable=False, comment='更新時間')


class Room(User):
    __tablename__ = 'room'

    user_id = Column(UUID, comment='fk')
    id = Column(ForeignKey('users.id', ondelete='SET NULL'), primary_key=True, server_default=text("gen_random_uuid()"), comment='pk')
    is_in = Column(Boolean, nullable=False)
    create_dt = Column(Date, nullable=False)
    update_dt = Column(Date, nullable=False)
