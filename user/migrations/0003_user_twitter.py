# Generated by Django 3.2.7 on 2021-10-06 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_web_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
