# Generated by Django 4.0.1 on 2022-03-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdiscord', '0004_delete_comentarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nambre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('website', models.CharField(max_length=120)),
                ('comentario', models.TextField()),
            ],
            options={
                'verbose_name': 'Comement',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
