# Generated by Django 3.2.5 on 2021-08-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_move_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
