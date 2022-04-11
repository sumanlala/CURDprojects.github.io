# Generated by Django 4.0.2 on 2022-04-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField(max_length=10)),
                ('course', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('assignment1', models.IntegerField()),
                ('assignment2', models.IntegerField()),
                ('assignment3', models.IntegerField()),
                ('assignment4', models.IntegerField()),
            ],
        ),
    ]
