# Generated by Django 5.1.1 on 2024-09-18 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbi', '0010_remove_area_area_area_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='nomedaempresa',
        ),
    ]
