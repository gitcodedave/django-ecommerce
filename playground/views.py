from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests
import logging

logger = logging.getLogger(__name__) # translates to playground.views

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2') # Simulating a 2 second delay
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render( request, 'hello.html', {'name': data} )

# # Same but class based view
# class HelloView(APIView):
#     @method_decorator(cache_page( 5 * 60 ))
#     def get(self, request):
#         response = requests.get('https://httpbin.org/delay/2') # Simulating a 2 second delay
#         data = response.json()
#         return render( request, 'hello.html', {'name': data} )

# Function based view
# @cache_page( 5 * 60 ) # 5 minutes
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2') # Simulating a 2 second delay
#     data = response.json()
#     return render( request, 'hello.html', {'name': data} )

    # Without decorator:
    # key = 'httpbin_result'
    # if cache.get('httpbin_result') is None:
    #     response = requests.get('https://httpbin.org/delay/2') # Simulating a 2 second delay
    #     data = response.json()
    #     cache.set(key, data)


    # notify_customers.delay('Hello')

    # CODE FOR SENDING AN EMAIL
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html', # Relative to inside the templates file
    #         context={'name': 'David'} # context is how you send the variables to the html file
    #     )
    #     # message = EmailMessage('Hi Dave', 'This is me attaching a file', 'davidortegacode@gmail.com', ['davidortegacode@gmail.com'])
    #     # message.attach_file('playground/static/images/Trinity-Matrix-Carrie-Anne-Moss-h2.jpg')
    #     message.send(['davidortegacode@gmail.com']) # The BaseEmailMessage class requires the 'to:' list
    #     # send_mail('Hi Dave', 'This is a test from your email server', 'davidortegacode@gmail.com', ['davidortegacode@gmail.com'])
    # except BadHeaderError:
    #     pass
    #  return render( request, 'hello.html', {'name': data} )
