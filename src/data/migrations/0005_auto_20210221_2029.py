# Generated by Django 3.1.7 on 2021-02-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20210220_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleauthor',
            name='url',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddConstraint(
            model_name='articleauthor',
            constraint=models.UniqueConstraint(condition=models.Q(url__isnull=False), fields=('url',), name='unique__url__when__url__not_null_on_data_articleauthor'),
        ),
    ]