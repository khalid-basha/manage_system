# Generated by Django 4.1.3 on 2022-12-09 13:53

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('school_system', '0010_alter_user_mobile_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_num',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=13, null=True, region=None, unique=True),
        ),
    ]
