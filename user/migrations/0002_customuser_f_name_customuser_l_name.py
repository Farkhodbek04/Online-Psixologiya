# Generated by Django 5.0.6 on 2024-05-22 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='f_name',
            field=models.CharField(default='deafault', max_length=30),
        ),
        migrations.AddField(
            model_name='customuser',
            name='l_name',
            field=models.CharField(default='default', max_length=30),
        ),
    ]