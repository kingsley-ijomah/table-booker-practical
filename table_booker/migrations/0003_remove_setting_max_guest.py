# Generated by Django 3.0.8 on 2021-06-18 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table_booker', '0002_auto_20210613_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='max_guest',
        ),
    ]