# Generated by Django 4.0.3 on 2022-04-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
