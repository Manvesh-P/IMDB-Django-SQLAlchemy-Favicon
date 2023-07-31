from django.db import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, 
                        Integer, 
                        String, 
                        ForeignKey)
from sqlalchemy.orm import relationship
# Create your models here.

Base = declarative_base()

class Organisation(Base):
    __tablename__ = 'organisation'

    org_id = Column(Integer(), primary_key=True, autoincrement=True)
    org_name = Column(String(500))

    r_user = relationship('User', back_populates='r_organisation', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return 'User(org_id=%d, org_name=%s)' % (self.org_id, self.org_name)
    

class User(Base):
    __tablename__ = 'user'
    # __tablename__ = '_user'

    user_uid = Column(Integer(), primary_key=True, autoincrement=True)
    # user_id = Column(Integer, primary_key=True, autoincrement=True)
    # user_id = Column(Integer())
    org_id = Column(Integer(), ForeignKey('organisation.org_id'))
    user_id = Column(Integer())
    user_created_date = Column(String(30))
    user_username = Column(String(500))
    user_password = Column(String(500))
    user_role = Column(String(500))
    user_approver_count = Column(String(50))

    # r_model = relationship('Model', back_populates='r_user', cascade='all, delete, delete-orphan')

    r_organisation = relationship("Organisation", back_populates='r_user')

    def __repr__(self):
        return "<User(user_uid='%d', org_id='%d', user_id='%d', user_created_date='%s', user_username='%s', user_password='%s', user_role='%s', user_approver_count='%s')>" % \
            (self.user_uid, self.org_id, self.user_id, self.user_created_date, self.user_username, self.user_password, self.user_role, self.user_approver_count)


# class Organisation(Base):
#     __tablename__ = 'organisation'
#     org_id = Column(Integer(), primary_key=True, autoincrement=True)
#     org_name = Column(String(500))

#     r_user = relationship("User", back_populates='r_organisation', cascade="all, delete, delete-orphan")

#     def __repr__(self):
#         return "<User(org_id='{}', org_name='{}')>"\
#                 .format(self.org_id, self.org_name)

# class User(Base):
#     __tablename__ = 'user'
#     user_uid = Column(Integer(), primary_key=True, autoincrement=True)
#     org_id = Column(Integer(), ForeignKey('organisation.org_id'))
#     user_id = Column(Integer())
#     user_created_date = Column(String(30))
#     user_username = Column(String(500))
#     user_password = Column(String(500))
#     user_role = Column(String(500))
#     user_approver_count = Column(String(50))

#     # r_model = relationship("Model", back_populates='r_user', cascade="all, delete, delete-orphan")

#     r_organisation = relationship("Organisation", back_populates='r_user')

#     def __repr__(self):
#         return "<User(user_uid='{}', org_id='{}', user_id='{}', user_created_date='{}', user_username='{}', user_password='{}', user_role='{}', user_approver_count='{}')>"\
#                 .format(self.user_uid, self.org_id, self.user_id, self.user_created_date, self.user_username, self.user_password, self.user_role, self.user_approver_count)
