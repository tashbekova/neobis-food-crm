# Generated by Django 2.0.6 on 2018-07-17 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0006_auto_20180717_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='waiter',
            new_name='role',
        ),
    ]
