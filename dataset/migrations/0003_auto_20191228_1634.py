# Generated by Django 2.2.5 on 2019-12-28 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0002_auto_20191228_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datafile',
            name='file',
        ),
        migrations.AddField(
            model_name='datafile',
            name='path',
            field=models.CharField(default='1', max_length=256),
            preserve_default=False,
        ),
    ]
