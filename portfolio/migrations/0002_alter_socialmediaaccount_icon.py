# Generated by Django 4.2 on 2023-04-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='icon',
            field=models.ImageField(upload_to='social_media_accounts/icons/'),
        ),
    ]