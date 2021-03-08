# Generated by Django 3.1.7 on 2021-03-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок', max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(help_text='Название группы', max_length=75, unique=True, verbose_name='Группа')),
                ('description', models.TextField(blank=True, help_text='Описание группы', verbose_name='Описание')),
            ],
        ),
    ]
