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
            logging.info("SAVE " + str(user))
            return True, user
        except Exception as e:
            logging.error("SAVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def edit(cls, code, user_name, password, active):
        try:
            # validation
            user = UserBl.find_by_code(code)
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
    def remove(cls, code):
        try:
            # validation
            user = UserBl.remove(code)
            logging.info("REMOVE " + user)
            return True, user
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def find_all(cls):
        try:
            user_list = UserBl.find_all()
            logging.info("FINDALL")
            return user_list
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def find_by_code(cls, code):
        try:
            user = UserBl.find_by_code(User)
            logging.info("FINDALL")
            return user
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)
