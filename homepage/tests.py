from django.test import TestCase
from django.apps import apps


class SanityTestCase(TestCase):
	def test_homepage_app_loaded(self):
		"""Sanity check: homepage app should be loaded."""
		self.assertTrue(apps.is_installed('homepage'))


class WeatherViewTests(TestCase):
	def test_get_homepage_renders_input_and_button(self):
		"""GET / should render the input field and button."""
		response = self.client.get('/')
		self.assertContains(response, 'name="location"')
		self.assertContains(response, 'Check Weather')

	def test_get_homepage_with_location_shows_weather(self):
		"""GET /?location=London should show weather status for London."""
		response = self.client.get('/', {'location': 'London'})
		# Should still show the input field and button for further queries
		self.assertContains(response, 'name="location"')
		self.assertContains(response, 'Check Weather')
		# Should show the location somewhere in the weather result
		self.assertContains(response, 'London')