# Generated by Django 4.1 on 2022-08-19 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_tag_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
    ]