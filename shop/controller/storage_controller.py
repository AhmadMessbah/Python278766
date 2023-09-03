import logging

from shop.model.bl.storage_bl import StorageBl
from shop.model.entity.storage import Storage


class UserController:
    @classmethod
    def save(cls, stuff_code,count,date_time,t_type):
        try:
            # validation
            storage = Storage(stuff_code,count,date_time,t_type)
            StorageBl.save(storage)
            logging.info("SAVE " + str(storage))
            return True, storage
        except Exception as e:
            logging.error("SAVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def edit(cls, stuff_code,count,date_time,t_type):
        try:
            # validation
            storage = StorageBl.find_by_code(stuff_code)
            storage.stuff_code = stuff_code
            storage.count = count
            storage.date_time = date_time
            storage.t_type = t_type
            storage = StorageBl.edit(storage)
            logging.info("EDIT " + storage)
            return True, storage
        except Exception as e:
            logging.error("EDIT-ERROR" + str(e))
            False, str(e)

    @classmethod
    def remove(cls, code):
        try:
            # validation
            storage = StorageBl.remove(code)
            logging.info("REMOVE " + storage)
            return True, storage
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def find_all(cls):
        try:
            storage_list = StorageBl.find_all()
            logging.info("FINDALL")
            return storage_list
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)

    @classmethod
    def find_by_code(cls, code):
        try:
            storage = StorageBl.find_by_code(Storage)
            logging.info("FINDALL")
            return storage
        except Exception as e:
            logging.error("REMOVE-ERROR" + str(e))
            False, str(e)
