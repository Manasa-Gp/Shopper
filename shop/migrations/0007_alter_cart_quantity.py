# Generated by Django 4.2 on 2023-04-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_costumers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]