# Generated by Django 5.1.4 on 2024-12-14 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_initial'),
        ('quib', '0003_remove_quibmodel_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='quibmodel',
            name='comments',
            field=models.ManyToManyField(
                blank=True,
                related_name='comments',
                to='comment.commentmodel',
                verbose_name='comments',
            ),
        ),
    ]
