# Generated by Django 4.1.4 on 2022-12-31 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_userdata_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='qa',
            name='USERNAME',
            field=models.CharField(blank=True, max_length=20, verbose_name='使用者名稱'),
        ),
        migrations.AlterField(
            model_name='qa',
            name='QUESTIONS',
            field=models.CharField(blank=True, max_length=500, verbose_name='問題回報'),
        ),
    ]
