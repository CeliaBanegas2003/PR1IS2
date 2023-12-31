# Generated by Django 4.2.5 on 2023-09-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0004_inforequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='slug',
        ),
        migrations.AlterField(
            model_name='cruise',
            name='destinations',
            field=models.ManyToManyField(related_name='cruises', to='relecloud.destination'),
        ),
    ]
