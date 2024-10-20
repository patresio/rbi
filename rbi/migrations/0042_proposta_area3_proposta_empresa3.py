# Generated by Django 4.2.16 on 2024-10-12 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbi', '0041_componente_slug_proposta_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposta',
            name='Area3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_empresa3', to='rbi.area'),
        ),
        migrations.AddField(
            model_name='proposta',
            name='Empresa3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_empresa2', to='rbi.empresa'),
        ),
    ]
