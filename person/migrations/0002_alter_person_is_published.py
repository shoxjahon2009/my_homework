# Generated by Django 5.0.6 on 2024-06-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
