from arrested import Resource
from arrested.contrib.kim_arrested import KimEndpoint
from arrested.contrib.sql_alchemy import DBListMixin, DBCreateMixin, DBObjectMixin

from posts.models import db, Post
from .mappers import PostMapper

posts_resource = Resource('posts', __name__, url_prefix='/posts')


class PostsIndexEndpoint(KimEndpoint, DBListMixin, DBCreateMixin):

    name = 'list'
    many = True
    mapper_class = PostMapper
    model = Post

    def get_query(self):

        stmt = db.session.query(Post)
        return stmt


class PostsObjectEndpoint(KimEndpoint, DBObjectMixin):

    name = 'object'
    url = '/<string:obj_id>'
    mapper_class = PostMapper
    model = Post

    def get_query(self):

        stmt = db.session.query(Post)
        return stmt


#class PostsLikeEndpoint(KimEndpoint, DBCreateMixin):
#
#    name = 'object'
#    url = '/<string:obj_id>/<action>'
#    mapper_class = PostMapper
#    model = Post
#
#    def like_action(obj_id, action):
#        post = Post.query.filter_by(id=obj_id).first_or_404()
#        if action == 'like':
#            current_user.like_post(post)
#            db.session.commit()
#        if action == 'unlike':
#            current_user.unlike_post(post)
#            db.session.commit()
#        return post
#
#    def get_query(self):
#
#        stmt = db.session.query(Post)
#        return stmt


posts_resource.add_endpoint(PostsIndexEndpoint)
posts_resource.add_endpoint(PostsObjectEndpoint)
#posts_resource.add_endpoint(PostsLikeEndpoint)
