# Generated by Django 2.2.11 on 2020-05-12 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_auto_20200512_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='talk_type',
        ),
    ]