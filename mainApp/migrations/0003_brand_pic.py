# Generated by Django 4.1.6 on 2023-08-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_rename_discription_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products'),
        ),
    ]