from django.test import SimpleTestCase
from django.urls import reverse, resolve
from food_diary_base.views import home, add_product, log_in, productCreate, diary



class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_diary_url(self):
        url = reverse('diary')
        self.assertEquals(resolve(url).func, diary)

    def test_add_product_url(self):
        url = reverse('add_product')
        self.assertEquals(resolve(url).func, add_product)

    def test_log_in_url(self):
        url = reverse('log_in')
        self.assertEquals(resolve(url).func, log_in)

    def test_product_create_url(self):
        url = reverse('product-create')
        self.assertEquals(resolve(url).func, productCreate)
