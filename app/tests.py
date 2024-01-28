from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Message


class SendMessageTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('send-message')

    def test_send_message_success(self):
        """
        Test that sending a valid message through the SendMessage API endpoint results in a successful creation.
        """
        data = {'message': 'Test message'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_send_message_failure(self):
        """
        Test that sending invalid data to the SendMessage API endpoint results in a validation error.
        """
        invalid_data = {'invalid_key': 'Invalid message data'}  # Invalid data to trigger a validation error
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReceiveMessageTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('receive')

    def test_receive_message_success(self):
        """
        Test that receiving a valid message through the ReceiveMessage API endpoint updates the existing message successfully.
        """
        # Assuming there's an existing message in the database with ID=1
        existing_message = Message.objects.create(message='Existing message')
        data = {'id': existing_message.id, 'message': 'Updated message'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Message.objects.get(id=existing_message.id).message, 'Updated message')

    def test_receive_message_not_found(self):
        """
        Test that receiving a message with a non-existent ID through the ReceiveMessage API endpoint results in a 404 error.
        """
        non_existent_id = 9999  # Assuming there's no message with ID=9999
        data = {'id': non_existent_id, 'message': 'Update non-existent message'}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_receive_message_invalid_data(self):
        """
        Test that receiving invalid data through the ReceiveMessage API endpoint results in a validation error.
        """
        invalid_data = {'invalid_key': 'Invalid data'}  # Invalid data to trigger a validation error
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
