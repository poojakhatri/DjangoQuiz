# Generated by Django 2.2.6 on 2019-10-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20191019_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='math',
            name='id',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='id',
        ),
        migrations.AddField(
            model_name='math',
            name='test_id',
            field=models.CharField(default=1, max_length=30, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stat',
            name='test_id',
            field=models.CharField(default=4, max_length=30, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
