# Generated by Django 4.2.4 on 2024-04-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
