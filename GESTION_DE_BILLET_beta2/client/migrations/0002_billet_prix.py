# Generated by Django 4.1.7 on 2023-04-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billet',
            name='prix',
            field=models.FloatField(default=0),
        ),
    ]