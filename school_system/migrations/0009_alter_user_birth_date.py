# Generated by Django 4.1.3 on 2022-12-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_system', '0008_alter_course_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default='1999-09-09', null=True),
        ),
    ]
