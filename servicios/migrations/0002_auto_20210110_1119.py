# Generated by Django 3.0.5 on 2021-01-10 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='Biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='Formacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
