# Generated by Django 2.2.11 on 2020-07-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkschedule',
            name='talk_url',
            field=models.CharField(default='', max_length=30),
        ),
    ]