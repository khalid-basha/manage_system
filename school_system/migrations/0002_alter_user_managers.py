# Generated by Django 4.1.3 on 2022-11-29 21:45

from django.db import migrations
import school_system.models


class Migration(migrations.Migration):

    dependencies = [
        ('school_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', school_system.models.UserManager()),
            ],
        ),
    ]
