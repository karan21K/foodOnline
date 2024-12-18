# Generated by Django 5.1.3 on 2024-11-24 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='fooditem',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
