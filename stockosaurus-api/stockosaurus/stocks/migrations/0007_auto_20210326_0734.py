# Generated by Django 3.1.7 on 2021-03-26 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0006_remove_stockprice_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockprice',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='StockPrice', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
