# Generated by Django 3.2.9 on 2022-09-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='deadline_at',
            field=models.CharField(max_length=255, null=True),
        ),
    ]