import logging

from shop.model.bl.user_bl import UserBl
from shop.model.entity.user import User


class UserController:
    @classmethod
    def save(cls, user_name, password):
        try:
            # validation
            user = User(user_name, password)
            UserBl.save(user)
            logging.info("SAVE " + user)
            return True, user
        except Exception as e:
            logging.error("SAVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def edit(cls, id, user_name, password, active):
        try:
            # validation
            user = UserBl.find_by_id(1)
            user.user_name = user_name
            user.password = password
            user.active = active
            user = UserBl.edit(user)
            logging.info("EDIT " + user)
            return True, user
        except Exception as e:
            logging.error("EDIT-ERROR" + str(e))
            False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            # validation
            user = UserBl.remove(id)
            logging.info("REMOVE " + user)
            return True, user
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def find_all(cls):
        try:
            user_list = UserBl.find_all(User)
            logging.info("FINDALL")
            return user_list
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            user = UserBl.find_by_id(User)
            logging.info("FINDALL")
            return user
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)
