# Generated by Django 3.1.7 on 2021-03-06 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210306_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='follow',
        ),
    ]
