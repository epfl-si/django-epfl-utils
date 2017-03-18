from django.test import TestCase, RequestFactory
from nose.tools import assert_equal
from mock import Mock
from epflutils.decorators import cache_anonymous_user
from django.contrib.auth.models import AnonymousUser, User


class DecoratorTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()

    def test_cache_anonymous_user(self):

        request = self.factory.get(
            '/',
        )
        request.user = self.user
        request.LANGUAGE_CODE = 'fr'


        request2 = self.factory.get(
            '/',
        )
        request2.user = User.objects.create_user(
            username='jacob', email='jacob', password='top_secret')

        request2.LANGUAGE_CODE = 'fr'

        homepagedecorator1 = cache_anonymous_user(timeout=60*2, cache='default')(request)
        decorator2 = cache_anonymous_user(timeout=60*2, cache='default')(request2)
