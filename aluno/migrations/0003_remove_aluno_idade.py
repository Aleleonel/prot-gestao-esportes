# Generated by Django 2.2 on 2019-04-23 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_aluno_idade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='idade',
        ),
    ]
