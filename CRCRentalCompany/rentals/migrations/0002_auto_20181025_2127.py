# Generated by Django 2.1.1 on 2018-10-25 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customerAddress',
            new_name='customer_address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customerBirthday',
            new_name='customer_birthday',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customerGender',
            new_name='customer_gender',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customerName',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customerOccupation',
            new_name='customer_occupation',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customerPhone',
            new_name='customer_phone',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='carId',
            new_name='car_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customerId',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='orderCreateDate',
            new_name='order_create_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pickupDate',
            new_name='pickup_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pickupStoreId',
            new_name='pickup_store_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='returnDate',
            new_name='return_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='returnStoreId',
            new_name='return_store_id',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='storeAddress',
            new_name='store_address',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='storeCity',
            new_name='store_city',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='storeName',
            new_name='store_name',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='storePhone',
            new_name='store_phone',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='storeState',
            new_name='store_state',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='bodyType',
            new_name='body_type',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='driveType',
            new_name='drive_type',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='fuelType',
            new_name='fuel_type',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='tankCapacity',
            new_name='tank_capacity',
        ),
    ]
