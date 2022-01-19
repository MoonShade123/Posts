from kim import field

from .base import BaseMapper

from posts.models import Post


class PostMapper(BaseMapper):
    __type__ = Post

    title = field.String()
    body = field.String()


