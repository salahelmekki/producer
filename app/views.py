from email import message

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
import requests
from .models import Message
from .serializers import MessageSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, views


class SendMessage(views.APIView):
    """
    API endpoint that send messages to the consumer
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                response = requests.post('http://127.0.0.1:8001/consumer/message',
                                         data={'id': serializer.data['id'], 'message': serializer.data['message'],
                                               'webhook_url': 'http://127.0.0.1:8000/producer/reciever'})
                response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            except requests.exceptions.RequestException as e:
                # Handle any exceptions that may occur during the request
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReceiveMessage(views.APIView):
    """
    Webhook that receiver data from consumer and edit message in database
    """
    def post(self, request):
        # Deserialize the data received in the request
        serializer = MessageSerializer(data=request.data)

        # Check if the data is valid
        if serializer.is_valid():
            # Extract the ID and message from the deserialized data
            print(serializer.data)
            message_id = serializer.validated_data.get('id')
            new_message = serializer.validated_data.get('message')
            # Assuming you have a Message model with a field 'id' to match against
            try:
                # Retrieve the existing message with the provided ID
                existing_message = Message.objects.get(id=request.data['id'])

                # Update the message with the new value
                existing_message.message = new_message
                existing_message.save()

                return Response({'status': 'Message updated successfully'}, status=status.HTTP_200_OK)

            except Message.DoesNotExist:
                # Handle the case where no message with the given ID is found
                return Response({'status': 'Message not found'}, status=status.HTTP_404_NOT_FOUND)

        # Handle the case where the provided data is not valid
        return Response({'status': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

