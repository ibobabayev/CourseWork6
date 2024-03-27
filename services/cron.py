from django.core.mail import send_mail
from django.conf import settings
from services.models import Client

def my_scheduled_job():
    print('Hello')
#
# def my_scheduled_job():
#     Client.obejcts.create(email='jack@mail.com',fio='jack logan',comment='bro')