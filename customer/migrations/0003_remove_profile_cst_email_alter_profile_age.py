# Generated by Django 4.1 on 2022-08-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_profile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cst_email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
