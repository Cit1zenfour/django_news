# Generated by Django 3.0.6 on 2020-06-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200605_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
