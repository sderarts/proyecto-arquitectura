# Generated by Django 4.1.3 on 2022-11-09 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_customer_passw'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]