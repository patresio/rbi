# Generated by Django 5.1.1 on 2024-09-18 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbi', '0018_remove_tag_empresa1_alter_tag_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='Empresa1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='area_empresa1', to='rbi.empresa'),
        ),
    ]
