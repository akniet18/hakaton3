# Generated by Django 2.2.7 on 2019-11-16 12:03

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191116_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=users.models.user_photos_dir),
        ),
    ]
