from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import APIClient

# Create your tests here.
class TestVocabView(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_vocab_view(self):
        endpoint = reverse('vocab')
        expected_output = {'message' : 'Some secret'}
        response = self.client.get(endpoint, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_output)