Producer
Producer is a Django project that provides an API endpoint to send messages and trigger webhooks. It allows users to post messages, and upon successful saving of the message, it sends a webhook to a specified URL.

Features
Send Messages: Post messages to the API endpoint.
Webhook Trigger: Upon successful message creation, a webhook is sent to a specified URL.
Getting Started
These instructions will help you set up the project and run it on your local machine.

Prerequisites
Python 3.x
Django
Django Rest Framework


Installation
Clone the repository:
cd producer
create venv
python3 -m venv venv
soource venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

The API will be available at http://127.0.0.1:8000/producer/message.

To send a message, make a POST request to the API endpoint:
curl -X POST http://127.0.0.1:8000/producer/message -d "message=YourMessage"
Upon successful creation of the message, a webhook will be sent to the specified URL.

Configuration
Update the WEBHOOK_URL variable in views.py to specify the default webhook URL.
Running Tests
Run tests using the following command:

bash
Copy code
python manage.py test producer
Contributing
If you'd like to contribute to this project, please follow the Contributing Guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to Django and Django Rest Framework for making web development in Python delightful.
