# Generated by Django 3.1.4 on 2020-12-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20201219_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercompanyinfo',
            name='logo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Customer_company_logo'),
        ),
    ]
