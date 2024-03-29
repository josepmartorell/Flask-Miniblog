import unittest

from app.auth.models import User
from app.models import Post
from . import BaseTestClass


class BlogClientTestCase(BaseTestClass):

    def test_index_with_no_posts(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'No posts', res.data)

    def test_index_with_posts(self):
        with self.app.app_context():
            admin = User.get_by_email('admin@xyz.com')
            post = Post(user_id=admin.id, title='Test post', content='Lorem Ipsum')
            post.save()
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertNotIn(b'No posts', res.data)

    def test_redirect_to_login(self):
        res = self.client.get('/admin/')
        self.assertEqual(302, res.status_code)
        self.assertIn('login', res.location)

    def test_unauthorized_access_to_admin(self):
        self.login('guest@xyz.com', '1111')
        res = self.client.get('/admin/')
        self.assertEqual(401, res.status_code)
        self.assertIn(b'Ooops!! You do not have access permissions', res.data)

    def test_authorized_access_to_admin(self):
        self.login('admin@xyz.com', '1111')
        res = self.client.get('/admin/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Posts', res.data)
        self.assertIn(b'Users', res.data)


if __name__ == '__main__':
    unittest.main()
