# Generated by Django 4.0.5 on 2023-04-11 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_customer_email_alter_customer_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
