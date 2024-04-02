import smtplib
from django.core.mail import send_mail
from django.conf import settings
from services.models import Client,Message,Newsletter,Logs
from datetime import datetime,timedelta,timezone
from django.utils import timezone



# def my_scheduled_job():
#     Client.objects.create(email='jack@mail.com',fio='jack logan',comment='bro')

def send_email():

    clients = Client.objects.all()
    clients_email = []
    for client in clients:
        clients_email.append(getattr(client,'email'))

    messages = Message.objects.all()
    message_subject = []
    message_body = []
    for message in messages:
        message_subject.append(getattr(message,'subject'))
        message_body.append(getattr(message,'body'))

    newsletters = Newsletter.objects.all()
    now = datetime.now()


    for newsletter in newsletters:
        # Очень много if-elif. Надо подумать, как правильно сделать!
        if newsletter.start_time < now < newsletter.end_time :
            for i in range(len(message_subject)):
                newsletter.status = 'запущена'
                try:
                    send_mail(
                        subject=message_subject[i],
                        message=message_body[i],
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=clients_email,
                        fail_silently=False
                        )
                    attempt = True
                    response = 'Рассылка успешно отправлена'
                except smtplib.SMTPException as e:
                    attempt = False
                    response = f'Ошибка при отправке письма: {str(e)}'

                finally:
                    for client in newsletter.client.all():
                        (Logs.objects.create(attempt=attempt,attempt_time=timezone.localtime(),response=response,newsletter=newsletter,client=client)).save()

        elif now > newsletter.end_time:
            newsletter.status = 'завершена'

        elif now < newsletter.start_time :
            newsletter.status = 'создана'

        # if newsletter.periodicity == 'раз в день':
        #     newsletter.start_time += datetime.timedelta(days=1,hours=0,minutes=0)
        # elif newsletter.periodicity == 'раз в неделю':
        #     newsletter.start_time += datetime.timedelta(days=7,hours=0,minutes=0)
        # elif newsletter.periodicity == 'раз в месяц':
        #     newsletter.start_time += datetime.timedelta(days=30,hours=0,minutes=0)

        newsletter.save()