# Generated by Django 5.0 on 2023-12-10 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
