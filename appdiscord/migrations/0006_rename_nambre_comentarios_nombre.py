# Generated by Django 4.0.1 on 2022-03-24 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdiscord', '0005_comentarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='nambre',
            new_name='nombre',
        ),
    ]
