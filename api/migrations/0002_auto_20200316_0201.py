# Generated by Django 2.1.2 on 2020-03-16 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='duration',
            new_name='operator',
        ),
    ]
