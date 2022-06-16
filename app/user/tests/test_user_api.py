"""
 Test for the user API
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create and return a new user model"""
    return get_user_model.objects.create_user(**params)

class PublicUserApiTest(TestCase):
    """Test the public feature of api"""

    def setUp(self):
        self.client = APIClient()

    def test_user_created_succesfull(self):
        """Test creating a user is successful"""
        paylod = {
            'email': 'test@example.com',
            'passsword': 'test1234',
            'name': 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, paylod)
        self.assertEqual(self.status_code, status.HTTP_201_CREATED)
        user = get_user_model.objects.get(email=paylod['email'])
        self.assertTrue(user.check_password(paylod['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists"""
        paylod = {
            'email': 'test@example.com',
            'password': 'test1234',
            'name': 'Test Name'
        }
        create_user(paylod)
        res = self.client.post(CREATE_USER_URL, paylod)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password too short """
        paylod = {
            'email': 'test@example.com',
            'password': 'pw',
            'name': 'Test Name'
        }
        res = self.client.post(CREATE_USER_URL, paylod)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=paylod['email']
        ).exists()
        self.assertFalse(user_exists)
