# Generated by Django 3.2.5 on 2021-08-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_move_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]
