import unittest

from app import create_app, db
from app.auth.models import User


class BaseTestClass(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(settings_module="config.testing")
        self.client = self.app.test_client()

        # Create an application context
        with self.app.app_context():
            # Create the database tables
            db.create_all()
            # We create an administrator user
            BaseTestClass.create_user('admin', 'admin@xyz.com', '1111', True)
            # We create a guest user
            BaseTestClass.create_user('guest', 'guest@xyz.com', '1111', False)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # Drop all tables from the database
            db.session.remove()
            db.drop_all()

    @staticmethod
    def create_user(name, email, password, is_admin):
        user = User(name, email)
        user.set_password(password)
        user.is_admin = is_admin
        user.save()
        return user

    def login(self, email, password):
        return self.client.post('/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)
