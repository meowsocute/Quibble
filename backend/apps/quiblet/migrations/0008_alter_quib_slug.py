# Generated by Django 5.1.3 on 2024-12-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiblet', '0007_remove_quib_is_draft_quib_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quib',
            name='slug',
            field=models.SlugField(editable=False, max_length=25, verbose_name='slug'),
        ),
    ]