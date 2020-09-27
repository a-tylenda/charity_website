# Generated by Django 3.1.1 on 2020-09-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.IntegerField(choices=[(0, 'Fundacja'), (2, 'Zbiórka lokalna'), (1, 'Organizacja Pozarządowa')], default=0),
        ),
    ]
