# Generated by Django 3.2.7 on 2022-09-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0003_usercredentialsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorFeedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_feed', models.CharField(max_length=100)),
            ],
        ),
    ]