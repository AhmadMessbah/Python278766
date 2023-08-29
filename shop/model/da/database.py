import time

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import text, and_, or_

from mft.model.entity.base import Base

from sqlalchemy.orm import sessionmaker

from mft.model.entity.customer import Customer


# engine = create_engine('mysql+pymysql://root:root123@localhost:3306/mft', echo=True)

class DatabaseManager:
    def make_engine(self):
        self.engine = create_engine('mysql+pymysql://root:@localhost:3306/mft')

        # Create Tables
        Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save(self, entity):
        self.make_engine()
        entity = self.session.add(entity)
        self.session.commit()
        self.session.close()
        return entity

    def edit(self, entity):
        self.make_engine()
        entity = self.session.merge(entity)
        self.session.commit()
        self.session.close()
        return entity

    def remove(self, entity):
        self.make_engine()
        entity = self.session.delete(entity)
        self.session.commit()
        self.session.close()
        return entity

    def find_all(self, class_name):
        self.make_engine()
        entity_list = self.session.query(class_name).all()
        self.session.close()
        return entity_list


    def find_by_code(self, class_name, code):
        self.make_engine()
        entity = self.session.get(class_name, code)
        self.session.close()
        return entity


