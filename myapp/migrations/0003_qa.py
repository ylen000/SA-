# Generated by Django 4.1.4 on 2022-12-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_userdata_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUESTIONS', models.CharField(max_length=500, verbose_name='問題回報')),
            ],
        ),
    ]
