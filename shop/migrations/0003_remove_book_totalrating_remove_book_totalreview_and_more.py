# Generated by Django 4.2.14 on 2024-08-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_writer_institution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='totalrating',
        ),
        migrations.RemoveField(
            model_name='book',
            name='totalreview',
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
