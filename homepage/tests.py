from django.test import TestCase
from django.apps import apps

class SanityTestCase(TestCase):
	def test_homepage_app_loaded(self):
		"""Sanity check: homepage app should be loaded."""
		self.assertTrue(apps.is_installed('homepage'))