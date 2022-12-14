# Generated by Django 4.1.1 on 2022-09-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
