# Generated by Django 3.2.17 on 2023-05-10 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0008_auto_20230509_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='break_point',
            field=models.IntegerField(default=0),
        ),
    ]