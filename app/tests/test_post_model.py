import unittest

from app.auth.models import User
from app.models import Post
from . import BaseTestClass


class PostModelTestCase(BaseTestClass):
    """Post model test suite"""

    def test_title_slug(self):
        with self.app.app_context():
            admin = User.get_by_email('admin@xyz.com')
            post = Post(user_id=admin.id, title='Test post', content='Lorem Ipsum')
            post.save()
            self.assertEqual('test-post', post.title_slug)

    def test_title_slug_duplicated(self):
        with self.app.app_context():
            admin = User.get_by_email('admin@xyz.com')
            post = Post(user_id=admin.id, title='Test', content='Lorem Ipsum')
            post.save()
            post_2 = Post(user_id=admin.id, title='Test', content='Lorem Ipsum Lorem Ipsum')
            post_2.save()
            self.assertEqual('test-1', post_2.title_slug)
            post_3 = Post(user_id=admin.id, title='Test', content='Lorem Ipsum Lorem Ipsum')
            post_3.save()
            self.assertEqual('test-2', post_3.title_slug)
            posts = Post.get_all()
            self.assertEqual(3, len(posts))


if __name__ == '__main__':
    unittest.main()
