# Generated by Django 2.1.1 on 2018-10-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=30)),
                ('customerPhone', models.CharField(max_length=30)),
                ('customerAddress', models.CharField(max_length=50)),
                ('customerBirthday', models.DateField()),
                ('customerOccupation', models.CharField(max_length=30)),
                ('customerGender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderCreateDate', models.DateField()),
                ('pickupDate', models.DateField()),
                ('returnDate', models.DateField()),
                ('customerId', models.IntegerField()),
                ('carId', models.IntegerField()),
                ('pickupStoreId', models.IntegerField(null=True)),
                ('returnStoreId', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeName', models.CharField(max_length=40)),
                ('storeAddress', models.CharField(max_length=50)),
                ('storePhone', models.CharField(max_length=30)),
                ('storeCity', models.CharField(max_length=40)),
                ('storeState', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('series', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('engine', models.CharField(max_length=4)),
                ('fuelType', models.CharField(max_length=30)),
                ('tankCapacity', models.CharField(max_length=8)),
                ('power', models.CharField(max_length=6)),
                ('seats', models.IntegerField()),
                ('transmission', models.CharField(max_length=7)),
                ('bodyType', models.CharField(max_length=20)),
                ('driveType', models.CharField(max_length=3)),
                ('wheelbase', models.CharField(max_length=7)),
            ],
        ),
    ]
