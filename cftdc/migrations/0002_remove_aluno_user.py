# Generated by Django 5.0.3 on 2024-03-27 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cftdc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='user',
        ),
    ]