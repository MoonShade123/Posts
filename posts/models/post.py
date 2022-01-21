from .base import db, PostMixin

__all__ = ['Post']


class Post(PostMixin, db.Model):

    __tablename__ = 'post'

    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    likes = db.relationship('PostLike', backref='post', lazy='dynamic')
