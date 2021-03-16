from django.test import TestCase, Client
from django.urls import reverse
from food_diary_api.models import Profile, Product, Meal, Day
import json
from django.utils import timezone
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user('DefaultUser', 'def@user.com', 'defpass')
        Day.objects.create(
            date=timezone.now(),
            user=self.user
        )
        self.day = Day.objects.all()[0]
        self.day_url = reverse('day', args=[self.day.id])
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'Default',
            last_name = 'Popkins',
            email = 'def@user.com'
        )
        self.product = Product.objects.create(
            product_name='Pasta',
            calories = 400,
            proteins = 3,
            carbs = 40,
            fats = 4,
            amount = 5
        )
        # self.meal = Meal.objects.create(
        #     meal_name = 'BREAKFAST',
        #     products.set() = self.product,
        #     day = self.day
        #
        # )


    def test_diary_list_GET(self):
        response = self.client.get(reverse('diary'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary.html')

    def test_day_list_GET(self):
        response = self.client.get(reverse(self.day_url))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'day.html')
