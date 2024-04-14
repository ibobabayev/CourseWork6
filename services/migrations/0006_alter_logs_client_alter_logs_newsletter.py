# Generated by Django 5.0.3 on 2024-04-14 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.client', verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='newsletter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.newsletter', verbose_name='рассылка'),
        ),
    ]
