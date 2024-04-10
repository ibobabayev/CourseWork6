from django.db import models
from django.conf import settings

NULLABLE = {'null': True, 'blank': True}

class Client(models.Model):
    email = models.EmailField(verbose_name='почта',unique=True)
    fio = models.CharField(max_length=70,verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий',**NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,verbose_name='владелец',**NULLABLE)

    def __str__(self):
        return f'ФИО: {self.fio}, почта: {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=30,verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,verbose_name='владелец',**NULLABLE)

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Newsletter(models.Model):
    start_time = models.DateTimeField(verbose_name='время начала отправки рассылки')
    end_time = models.DateTimeField(verbose_name='время окончания отправки рассылки')

    daily = 'раз в день'
    weekly = 'раз в неделю'
    monthly = 'раз в месяц'
    Periodicity = [
        (daily,'раз в день'),(weekly,'раз в неделю'),(monthly,'раз в месяц')
    ]
    periodicity = models.CharField(max_length=20,verbose_name='периодичность',choices=Periodicity)

    finished = 'завершена'
    created = 'создана'
    launched = 'запущена'
    Status = [
        (finished, 'завершена'), (created, 'создана'), (launched, 'запущена')
    ]
    status = models.CharField(max_length=20,verbose_name='статус рассылки',choices=Status,default=created)

    client = models.ManyToManyField(Client,verbose_name='клиент',**NULLABLE)
    message = models.ForeignKey(Message,verbose_name='сообщение',on_delete=models.CASCADE,**NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,verbose_name='владелец',**NULLABLE)


    def __str__(self):
        return f'Время: {self.start_time} - {self.end_time}, статус рассылки: {self.status}, периодичность рассылки: {self.periodicity}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

        permissions = [
            ('change_status', 'Can change newsletters status'),
        ]


class Logs(models.Model):
    attempt = models.BooleanField(verbose_name='статус попытки')
    attempt_time = models.DateTimeField(verbose_name='дата и время последней попытки')
    response = models.CharField(max_length=100,verbose_name='ответ почтового сервера',**NULLABLE)

    newsletter = models.ForeignKey(Newsletter,verbose_name='рассылка',on_delete=models.CASCADE)
    client = models.ForeignKey(Client,verbose_name='клиент',on_delete=models.CASCADE)

    def __str__(self):
        return f'статус попытки: {self.attempt}, дата и время последней попытки: {self.attempt_time},ответ почтового сервера: {self.response}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


class Contact(models.Model):
    name = models.CharField(max_length=50,verbose_name='Имя')
    number = models.TextField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return f'{self.name} {self.number}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"