# Generated by Django 4.1.7 on 2023-05-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_reservationflight_reservationflightpredictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='route',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
