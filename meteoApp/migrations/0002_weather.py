# Generated by Django 3.1.4 on 2020-12-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meteoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
                ('time', models.CharField(max_length=25)),
                ('temperature', models.FloatField()),
                ('rain', models.FloatField()),
                ('pressure', models.FloatField()),
                ('wind', models.FloatField()),
            ],
        ),
    ]
