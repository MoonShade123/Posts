import datetime
from sqlalchemy_utils import EmailType, PasswordType
from sqlalchemy.ext.declarative import declared_attr

from . import db


class UserMixin(object):

    @declared_attr
    def id(cls):

        return db.Column(db.Integer, primary_key=True)

    @declared_attr
    def created_at(cls):

        return db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @declared_attr
    def updated_at(cls):

        return db.Column(db.DateTime, default=datetime.datetime.utcnow)

    name = db.Column(db.Unicode(255), nullable=False)
    email = db.Column(EmailType, nullable=False)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
        ],
    ))


class PostMixin(object):

    @declared_attr
    def id(cls):

        return db.Column(db.Integer, primary_key=True)

    @declared_attr
    def created_at(cls):

        return db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @declared_attr
    def updated_at(cls):

        return db.Column(db.DateTime, default=datetime.datetime.utcnow)
