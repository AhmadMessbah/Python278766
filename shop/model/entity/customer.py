from mft.model.entity.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mft.model.entity.invoice import Invoice


class Customer(Base):
    __tablename__ = 'customer'

    # id = Column(Integer, primary_key=True)
    # name = Column(String(30))
    # address = Column(String(50))
    # email = Column(String(50))

    def __repr__(self):
        return str(f"{self.id} {self.name}")

Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")
