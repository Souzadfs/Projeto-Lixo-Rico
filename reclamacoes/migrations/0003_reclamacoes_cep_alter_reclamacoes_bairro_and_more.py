# Generated by Django 4.2.5 on 2023-09-24 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moradores', '0003_morador_bairro'),
        ('reclamacoes', '0002_reclamacoes_data_criacao_reclamacoes_historico_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacoes',
            name='cep',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='bairro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moradores.bairro'),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='historico',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('verificado', 'Verificado'), ('resolvido', 'Resolvido'), ('nao_resolvido', 'Não Resolvido')], default='pendente', editable=False, max_length=20),
        ),
    ]
