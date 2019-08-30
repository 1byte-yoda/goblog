from unittest import TestCase
from app.models import User

class UserModelTestCase(TestCase):
    def test_password_setter(self):
        u = User(password='hardpassword')
        self.assertTrue(u.password_hash is not None)
    
    def test_password_no_getter(self):
        u = User(password='hardpassword')
        with self.assertRaises(AttributeError):
            u.password
    
    def test_password_verification(self):
        u = User(password='hardpassword')
        self.assertTrue(u.verify_password('hardpassword'))
        self.assertFalse(u.verify_password('wrongpassword'))

    def test_password_salts_random(self):
        u1 = User(password='password1')
        u2 = User(password='password1')
        self.assertTrue(u1.password_hash != u2.password_hash)