# Generated by Django 4.2.5 on 2023-09-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamacoes', '0003_reclamacoes_cep_alter_reclamacoes_bairro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacoes',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
    ]