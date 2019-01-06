# Generated by Django 2.1.4 on 2019-01-06 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resepti', '0010_auto_20190102_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('ing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resepti.Ingredient')),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resepti.Recipe')),
            ],
        ),
    ]