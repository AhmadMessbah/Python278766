from shop.model.entity.base import Base
from sqlalchemy import *


class Storage(Base):
    __tablename__ = 'storage_tbl'

    code = Column(Integer, primary_key=True)
    stuff_code = Column(Integer)
    # true == sell flase == stay
    t_type = Column(Boolean)
    count = Column(Integer)
    date_time = Column(TIMESTAMP)

    def __init__(self,stuff_code,count,date_time):
        self.stuff_code = stuff_code
        self.count = count
        self.date_time = date_time
        self.t_type = True

    def __repr__(self):
        return str(f"{self.code} {self.stuff_code} {self.t_type} {self.count} {self.date_time}")