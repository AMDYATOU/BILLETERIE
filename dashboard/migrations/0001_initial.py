# Generated by Django 4.1.7 on 2023-04-22 19:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cp', models.CharField(max_length=15)),
                ('telephone_cp', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='TG')),
                ('email_cp', models.EmailField(blank=True, max_length=254, null=True)),
                ('siege_cp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_grd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ville', models.CharField(max_length=100)),
            ],
        ),
    ]