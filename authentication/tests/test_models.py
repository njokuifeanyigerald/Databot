from rest_framework.test import APITestCase
from authentication.models import User


# rememeber to start with test
class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('gerald', 'b@gmail.com', '2123%^$&sn')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.email, 'b@gmail.com')
    
    def test_value_error_of_username(self):
        self.assertRaises(ValueError, User.objects.create_user,username="",email='b@gmail.com', password='2123%^$&sn')

    # just incase you want to use the message value error way
    def test_value_error_message_of_username(self):
        with self.assertRaisesMessage(ValueError, "The given username must be set"):
            User.objects.create_user(username="",email='b@gmail.com', password='2123%^$&sn')


    def test_value_error_of_email(self):
        self.assertRaises(ValueError, User.objects.create_user,username="gerald",email='', password='2123%^$&sn')

    def test_creates_superuser(self):
        user = User.objects.create_superuser('gerald', 'b@gmail.com', '2123%^$&sn')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, 'b@gmail.com')


    def test_value_error_message_of_is_staff(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
            User.objects.create_superuser(username="gerald",email='b@gmail.com', password='2123%^$&sn', is_staff=False)


    def test_value_error_message_of_is_superuser(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
            User.objects.create_superuser(username="gerald",email='b@gmail.com', password='2123%^$&sn', is_superuser=False)
    

    
    
    
        
