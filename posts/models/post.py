from .base import db, BaseMixin

__all__ = ['Post']


class Post(BaseMixin, db.Model):

    __tablename__ = 'post'

    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)
