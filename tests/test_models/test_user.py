#!/usr/bin/python3
""" let tes test our user class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """let the function test our users  """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """let tset our firs name  """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """let test our last name  """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """let test our email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """let test our email """
        new = self.value()
        self.assertEqual(type(new.password), str)
