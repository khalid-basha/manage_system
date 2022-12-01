# Generated by Django 4.1.3 on 2022-11-29 22:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('school_system', '0003_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_num',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=12, null=True, region=None, unique=True),
        ),
    ]