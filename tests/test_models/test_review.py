test_review.py
#!/usr/bin/python3
""" our test for our review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """let test our reviews based on our model """

    def __init__(self, *args, **kwargs):
        """lets add init in our program """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """lets add place and testes """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """lets test our review on our userid """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ lets test our text reviews """
        new = self.value()
        self.assertEqual(type(new.text), str)
