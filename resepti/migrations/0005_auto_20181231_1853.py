# Generated by Django 2.1.4 on 2018-12-31 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resepti', '0004_auto_20181231_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingred_amts',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='volume',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
