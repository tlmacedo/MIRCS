# Generated by Django 5.0.3 on 2024-03-27 02:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
                ('nomenclatura', models.TextField(max_length=80)),
                ('carga_horaria', models.IntegerField(default=0)),
                ('data_criacao', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=80)),
                ('rg', models.TextField(max_length=15)),
                ('cpf', models.TextField(max_length=11)),
                ('data_nascimento', models.DateField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]