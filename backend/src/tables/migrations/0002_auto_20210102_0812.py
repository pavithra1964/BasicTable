# Generated by Django 2.2.13 on 2021-01-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='Stu_Name',
            field=models.CharField(max_length=120),
        ),
    ]
