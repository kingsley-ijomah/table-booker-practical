# Generated by Django 3.0.8 on 2021-06-14 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table_booker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='postcode',
        ),
        migrations.AlterField(
            model_name='table',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='table_booker.Restaurant'),
        ),
    ]
