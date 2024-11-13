# Generated by Django 5.1.3 on 2024-11-11 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_profile_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]