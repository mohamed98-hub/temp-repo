# Generated by Django 4.1 on 2022-08-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrn', models.CharField(max_length=25)),
                ('psw', models.CharField(max_length=25)),
                ('age', models.IntegerField(max_length=3)),
                ('cst_email', models.EmailField(max_length=25)),
            ],
        ),
    ]