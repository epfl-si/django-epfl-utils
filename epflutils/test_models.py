from django.test import TestCase


class DjangoPermissionChecksTestCase(TestCase):

    def switch_language_and_redirect(self):
        self.assertTrue(True)

    def test_check(self):
        self.assertTrue(True)
