# Generated by Django 4.1 on 2022-08-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
