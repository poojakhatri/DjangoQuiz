# Generated by Django 2.2.6 on 2019-10-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='math',
            name='si_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='si_no',
            field=models.IntegerField(null=True),
        ),
    ]
