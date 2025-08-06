"""Test cases for the greeting app."""

from django.test import TestCase, Client
from django.urls import reverse


class GreetingTests(TestCase):
    """Tests for the index page and basic greeting behavior."""

    def setUp(self):
        """Set up the test client."""
        self.client = Client()

    def test_index_page(self):
        """Test that the index page returns 200 and displays 'Hello'."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello')
        self.assertTemplateUsed(response, 'index.html')


class GreetingFunctionalityTests(TestCase):
    """Tests for greeting-related functionality."""

    def setUp(self):
        """Set up the test client."""
        self.client = Client()

    def test_greeting(self):
        """Test that the greeting context variable is 'Hello'."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context['greeting'], 'Hello')
