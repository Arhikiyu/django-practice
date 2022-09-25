# Generated by Django 3.2.9 on 2022-09-25 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lunchmap', '0003_auto_20220925_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='idea_id',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='idea_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lunchmap.shop'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='txt',
            field=models.CharField(max_length=255, null=True),
        ),
    ]