# Generated by Django 5.0.3 on 2024-04-09 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_client_owner_message_owner_newsletter_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'permissions': [('change_status', 'Can change newsletters status')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
