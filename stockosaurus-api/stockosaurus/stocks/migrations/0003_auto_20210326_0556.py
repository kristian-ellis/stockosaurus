# Generated by Django 3.1.7 on 2021-03-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_stockprice_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprice',
            name='owner',
            field=models.TextField(default=None),
        ),
    ]
