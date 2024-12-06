# Generated by Django 5.1.3 on 2024-12-04 16:11

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiblet', '0016_alter_quib_id_alter_quib_slug_alter_quiblet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quib',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet='abcdefghijklmnopqrstuvwxyz0123456789',
                editable=False,
                length=7,
                max_length=7,
                prefix='',
                primary_key=True,
                serialize=False,
                verbose_name='id',
            ),
        ),
        migrations.AlterField(
            model_name='quiblet',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet='abcdefghijklmnopqrstuvwxyz0123456789',
                editable=False,
                length=7,
                max_length=7,
                prefix='',
                primary_key=True,
                serialize=False,
                verbose_name='id',
            ),
        ),
    ]