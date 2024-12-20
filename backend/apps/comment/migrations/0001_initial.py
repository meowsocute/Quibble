# Generated by Django 5.1.4 on 2024-12-14 02:43

import django_ltree.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('path', django_ltree.fields.PathField(unique=True)),
                (
                    'created_at',
                    models.DateTimeField(auto_now_add=True, verbose_name='create at'),
                ),
                ('content', models.TextField(verbose_name='content')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
