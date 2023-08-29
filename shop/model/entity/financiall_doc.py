from shop.model.entity.base import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'fin_doc_tbl'

    code = Column(Integer, primary_key=True)
    amount = Column(Integer)
    data_time = Column(String(30))
    User = Column(String(30))
    d_type = Column(String(30))
    description =Column(String(30))
    def __init__(self,code,amount,data_time,User,d_type,description):
        self.code= code
        self.amount=amount
        self.data_time=data_time
        self.User=User
        self.d_type=d_type
        self.description=description
        return str(f"{self.code} {self.amount} {self.data_time} {self.User}{self.d_type}{self.description}")
        self.active = True
        self.deleted = False


def __repr__(self):
    return str(f"{self.code} {self.amount} {self.data_time} {self.User}{self.d_type}{self.description}")
