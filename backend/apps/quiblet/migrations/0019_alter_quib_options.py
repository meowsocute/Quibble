# Generated by Django 5.1.3 on 2024-12-06 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiblet', '0018_alter_quib_quibber_alter_quib_quiblet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quib',
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Quib',
                'verbose_name_plural': 'Quibs',
            },
        ),
    ]
