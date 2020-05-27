# Generated by Django 2.0.1 on 2018-07-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0013_auto_20180719_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='category',
            field=models.CharField(choices=[('Bronze', 'Bronze - $500'), ('Silver', 'Silver - $1000'), ('Gold', 'Gold - $2500'), ('Diamond', 'Diamond - $3500'), ('Diversity', 'Diversity'), ('Special', 'Special'), ('Individual', 'Individual'), ('Other', 'Other')], max_length=15),
        ),
    ]
