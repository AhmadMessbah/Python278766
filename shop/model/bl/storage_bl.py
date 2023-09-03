from shop.model.da.database import DatabaseManager
from shop.model.entity.storage import Storage


class StorageBl:
    @classmethod
    def save(cls, storage):
        da = DatabaseManager()
        return da.save(storage)

    @classmethod
    def edit(cls, storage):
        da = DatabaseManager()
        return da.edit(storage)

    @classmethod
    def remove(cls, storage):
        da = DatabaseManager()
        user = da.find_by_code(Storage, storage)
        return da.remove(storage)

    @classmethod
    def find_all(cls):
        da = DatabaseManager()
        return da.find_all(Storage)

    @classmethod
    def find_by_code(cls, code):
        da = DatabaseManager()
        return da.find_by_code(Storage, code)