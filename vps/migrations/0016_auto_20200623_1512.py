# Generated by Django 2.2.5 on 2020-06-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0015_auto_20200623_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='annual',
            field=models.CharField(blank=True, max_length=256, verbose_name='年付'),
        ),
    ]
