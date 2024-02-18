test_place.py
#!/usr/bin/python3
"""our program that test our place class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ let the func test_place our model """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """let the func test our city model """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """lets the func test our user id model """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """let the func test our name in our model """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test the func on our descriptin model """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test the number of room in the func """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test how many bath room  """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test how many  guests find out """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test the price of theroom s """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test the highit based on the lattidued/nce """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """lets test the longtudie """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test our ids  amneditiy """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
