# Generated by Django 2.1.1 on 2018-09-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_auto_20180919_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='returnDate',
            field=models.IntegerField(),
        ),
    ]