from sqlalchemy import create_engine

from shop.model.entity.base import Base

from sqlalchemy.orm import sessionmaker



class DatabaseManager:
    def make_engine(self):
        self.engine = create_engine('mysql+pymysql://root:root123@localhost:3306/mft', echo=True)
        # self.engine = create_engine('mysql+pymysql://root:@localhost:3307/mft')

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

    def find_by(self, class_name, filter):
        self.make_engine()
        entity = self.session.query(class_name).filter(filter)
        self.session.close()
        return entity