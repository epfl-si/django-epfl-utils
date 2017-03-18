from django.test import TestCase

from example.exampleapp.models import NoAbstractLabelModel


class TestLabelModelTestCase(TestCase):

    def setUp(self):

        self.cat = NoAbstractLabelModel.objects.create(
            fr_label='Chat',
            en_label='Cat',
        )

    def test_switch_language_and_redirect(self):

        self.assertEqual(self.cat.fr_label, 'Chat')
        self.assertEqual(self.cat.en_label, 'Cat')
