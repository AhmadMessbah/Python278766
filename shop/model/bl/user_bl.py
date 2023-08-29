from shop.model.da.database import DatabaseManager
from shop.model.entity.user import User


class UserBl:
    @classmethod
    def save(cls, user):
        da = DatabaseManager()
        return da.save(user)

    @classmethod
    def edit(cls, user):
        da = DatabaseManager()
        return da.save(user)

    @classmethod
    def remove(cls, id):
        da = DatabaseManager()
        user = da.find_by_id(id)
        return da.remove(user)

    @classmethod
    def find_all(cls):
        da = DatabaseManager()
        return da.find_all(User)

    @classmethod
    def find_by_id(cls, id):
        da = DatabaseManager()
        return da.find_by_id(User, id)
