# Generated by Django 4.0.5 on 2022-06-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_usuario_bairro_usuario_celular_usuario_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cep',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
