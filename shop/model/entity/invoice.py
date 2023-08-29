import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from mft.model.entity.base import Base
from sqlalchemy.orm import relationship


class Invoice(Base):
    __tablename__ = 'invoices'

    code = Column(Integer, primary_key=True)
    inv_code = Column(Integer)
    custumer = Column(Integer)
    custumer_id = Column(Integer, ForeignKey('customer.id'))
    amount = Column(Integer)
    discount = Column(Integer)
    pure_price = Column(Integer)
    status = Column(bool)
    date_time = Column(datetime.datetime)
    description = Column(string(50))


    # customer = relationship("Customer", back_populates="invoices")

    def __repr__(self):
        return str(self.__dict__)
