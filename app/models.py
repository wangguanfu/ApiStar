from datetime import datetime
from sqlalchemy import Column, Integer, String, TEXT, VARCHAR, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Admin(Base):
    __tablename__ = "Admin"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(50))
    full_name = Column(VARCHAR(100))
    img_url = Column(TEXT)
    email = Column(VARCHAR(100))
    password = Column(String(200))
    at_register = Column(DateTime, default=datetime.now())

    def __init__(self, username, full_name, img_url, email, password):
        self.username = username
        self.full_name = full_name
        self.img_url = img_url
        self.email = email
        self.password = password

    def __repr__(self):
        return ('username {}'.format(self.username))


class Publisher(Base):
    __tablename__ = "Publisher"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(50), unique=True)
    full_name = Column(VARCHAR(100))
    img_url = Column(TEXT)
    email = Column(VARCHAR(100))
    password = Column(String(200))
    culinarys = relationship('Culinary', backref='Publisher')
    at_register = Column(DateTime, default=datetime.now())

    def __init__(self, username, full_name, img_url, email, password):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.img_url = img_url
        self.password = password

    def __repr__(self):
        return ('username {}'.format(self.username))


class Culinary(Base):
    __tablename__ = "Culinary"

    id = Column(Integer, primary_key=True)
    publisher = Column(VARCHAR(100), ForeignKey('Publisher.username'))
    culinary_name = Column(VARCHAR(100))
    description = Column(TEXT)
    location = Column(VARCHAR(100))
    img_url = Column(TEXT)
    at_created = Column(DateTime, default=datetime.now())

    def __init__(self, publisher, culinary_name, description, location, img_url):
        self.publisher = publisher
        self.culinary_name = culinary_name
        self.description = description
        self.location = location
        self.img_url = img_url

    def __repr__(self):
        return ('culinary_name {}'.format(self.culinary_name))
