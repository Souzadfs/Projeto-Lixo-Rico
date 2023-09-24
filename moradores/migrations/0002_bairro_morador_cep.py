# Generated by Django 4.2.5 on 2023-09-24 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
                ('logradouro', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='morador',
            name='cep',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
