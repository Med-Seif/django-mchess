# Generated by Django 3.2.5 on 2021-07-29 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
