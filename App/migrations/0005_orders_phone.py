# Generated by Django 3.0.5 on 2023-04-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
    ]