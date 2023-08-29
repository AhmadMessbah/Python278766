from shop.model.entity.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class User(Base):
    __tablename__ = 'user_tbl'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(30))
    password = Column(String(50))
    active = Column(Boolean)
    deleted = Column(Boolean)

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        self.active = True
        self.deleted = False

    def __repr__(self):
        return str(f"{self.id} {self.user_name} {self.password} {self.active}")
