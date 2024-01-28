from django.urls import path
from .views import SendMessage, ReceiveMessage

urlpatterns = [
    # url API post Message
    path('message', SendMessage.as_view(), name='send-message'),
    # url webhook receive
    path('reciever', ReceiveMessage.as_view(), name='receive')
]
