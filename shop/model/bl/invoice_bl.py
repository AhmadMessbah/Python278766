from shop.model.da.database import DatabaseManager
from shop.model.entity.customer import Customer
from shop.model.entity.invoice import Invoice


class InvoiceBl:
    db = Database(Invoice, "online_store", "invoice_tbl")

    @classmethod
    def save(cls, code):
        return cls.db.save(code)

    @classmethod
    def edit(cls, code):
        return cls.db.edit(code)

    @classmethod
    def remove(cls, code):
        return cls.db.remove(code)

    @classmethod
    def find_all(cls):
        return cls.db.find_all()

    @classmethod
    def find_by_inv_code(cls, inv_code):
        return cls.db.find_by_inv_code(inv_code)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        return cls.db.find_by_customer_id(customer_id)
