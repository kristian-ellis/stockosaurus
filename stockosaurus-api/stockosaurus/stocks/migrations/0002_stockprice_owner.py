# Generated by Django 3.1.7 on 2021-03-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockprice',
            name='owner',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
