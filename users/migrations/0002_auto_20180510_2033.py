# Generated by Django 2.0.5 on 2018-05-11 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employees',
            name='gender',
            field=models.TextField(blank=True, max_length=1),
        ),
    ]
