# Generated by Django 4.2.4 on 2023-10-25 14:39

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moradores', '0003_morador_bairro'),
        ('reclamacoes', '0005_merge_20231024_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacoes',
            name='cpf',
            field=cpf_field.models.CPFField(default='', max_length=14, verbose_name='cpf'),
        ),
        migrations.AddField(
            model_name='reclamacoes',
            name='cpfOpcional',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='bairro',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='moradores.bairro'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('verificando', 'Verificando'), ('resolvido', 'Resolvido')], default='pendente', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='tipo_reclamacao',
            field=models.CharField(choices=[('nao_recebi', 'Não recebi o saco verde'), ('caminhao_nao_passou', 'Caminhão não passou'), ('saco_rasgado', 'Saco rasgado'), ('sugestao', 'Sugestão'), ('outros', 'Outros')], default='outros', max_length=20),
        ),
    ]
