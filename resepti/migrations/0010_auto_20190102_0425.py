# Generated by Django 2.1.4 on 2019-01-02 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resepti', '0009_remove_ingredient_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
