# Generated by Django 3.0 on 2019-12-24 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='modofied',
            new_name='modified',
        ),
    ]
