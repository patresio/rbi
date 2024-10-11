# Generated by Django 4.2.16 on 2024-10-11 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbi', '0032_rename_empresa_area_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='rbi.empresa'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='Area2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_empresa2', to='rbi.area'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='Empresa2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_empresa1', to='rbi.empresa'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='tagequip2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_tagequip', to='rbi.tag'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='Dados',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dados_numeroproposta', to='rbi.proposta'),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='Tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag_proposta', to='rbi.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='Area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_tag', to='rbi.area'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='Empresa1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_empresa2', to='rbi.empresa'),
        ),
    ]
