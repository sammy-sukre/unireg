# Generated by Django 3.2.4 on 2021-08-16 09:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0002_auto_20210816_1220'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='User',
        ),
    ]
