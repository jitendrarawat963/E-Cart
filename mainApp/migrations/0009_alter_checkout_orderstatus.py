# Generated by Django 4.1.6 on 2023-08-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='orderStatus',
            field=models.IntegerField(choices=[(1, 'Order Placed'), (2, 'Ready To Dispatch'), (3, 'Dispatched'), (4, 'Out For Delivery'), (5, 'Delivered')], default=1),
        ),
    ]