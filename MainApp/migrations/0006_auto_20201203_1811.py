# Generated by Django 3.1 on 2020-12-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.CharField(choices=[('py', 'python'), ('cpp', 'C++'), ('js', 'JavaScript')], max_length=30),
        ),
    ]
