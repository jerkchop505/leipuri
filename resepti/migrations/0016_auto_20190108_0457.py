# Generated by Django 2.1.4 on 2019-01-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resepti', '0015_auto_20190107_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='calories_per_each',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='calories_per_gram',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
