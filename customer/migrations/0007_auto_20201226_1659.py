# Generated by Django 3.1.4 on 2020-12-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20201219_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercompanyinfo',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='Customer_company_logo'),
        ),
    ]