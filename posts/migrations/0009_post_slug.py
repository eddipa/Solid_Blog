# Generated by Django 4.1 on 2022-08-24 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='title1', unique=True),
            preserve_default=False,
        ),
    ]