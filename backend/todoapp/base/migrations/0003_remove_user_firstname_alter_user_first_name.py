# Generated by Django 4.1.1 on 2022-09-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_firstname_alter_user_email_alter_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
