# Generated by Django 3.2.7 on 2022-09-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0004_doctorfeedmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorfeedmodel',
            name='doctor_feed',
        ),
        migrations.AddField(
            model_name='doctorfeedmodel',
            name='Feedback',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
