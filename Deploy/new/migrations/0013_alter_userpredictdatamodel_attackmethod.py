# Generated by Django 3.2.7 on 2022-10-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0012_userpredictdatamodel_attackmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpredictdatamodel',
            name='AttackMethod',
            field=models.CharField(max_length=100),
        ),
    ]
