# Generated by Django 3.2.7 on 2022-10-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0009_remove_userpredictdatamodel_attackmethod'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpredictdatamodel',
            name='AttackMethod',
            field=models.CharField(default=1, max_length=100),
        ),
    ]