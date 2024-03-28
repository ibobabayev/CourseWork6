from django.core.mail import send_mail
from django.conf import settings
from services.models import Client,Message


# def my_scheduled_job():
#     Client.objects.create(email='jack@mail.com',fio='jack logan',comment='bro')
def send_email():
    clients = Client.objects.all()
    clients_email = []
    for client in clients:
        clients_email.append(getattr(client,'email'))

    message = Message.objects.all()
    message_subject = []
    message_body = []
    for i in message:
        message_subject.append(getattr(i,'subject'))
        message_body.append(getattr(i,'body'))

    send_mail(
            subject=message_subject,
            message=message_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[clients_email],
            )
    #
    # send_mail(
    #     subject='subject',
    #     message='body',
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list='ibish_acmilan@mail.ru',
    # )