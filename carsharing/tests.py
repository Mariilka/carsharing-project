from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
class StudentsViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_list(self):
        r = self.client.get('/api/carsharing/')
        print(r)

    def test_get_list(self):
        сategory = Category.objects.create(
            name="Комфорт"
        )

        car = Car.objects.create(
            name="Hyundai Solaris",
            category=category,
        )

        r = self.client.get('/api/cars/')
        data = r.json()
        print(data)

        assert car.name == data[0]['name']
        assert car.id == data[0]['id']
        assert car.category.id == data[0]['category']
        assert len(data) == 1