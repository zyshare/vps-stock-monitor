# Generated by Django 2.2.5 on 2020-06-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0014_auto_20200623_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.CharField(help_text='https://bwh88.net/aff.php?aff=991&pid=', max_length=256, verbose_name='网址'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='pid',
            field=models.IntegerField(blank=True, verbose_name='PID'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='route',
            field=models.CharField(choices=[('CN2-GT', 'CN2-GT'), ('CN2-GIA', 'CN2-GIA'), ('BGP', 'BGP'), ('PCCW', 'PCCW')], max_length=256, verbose_name='线路'),
        ),
    ]
