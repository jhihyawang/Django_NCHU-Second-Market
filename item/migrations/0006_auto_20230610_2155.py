# Generated by Django 3.1.2 on 2023-06-10 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20230610_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('pub_time',)},
        ),
        migrations.AddField(
            model_name='category',
            name='pub_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]