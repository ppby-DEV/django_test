# Generated by Django 3.0 on 2019-12-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fcuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='패스워드')),
                ('registered_dttm', models.DateTimeField(auto_now=True, verbose_name='등록시간')),
            ],
            options={
                'db_table': 'fastcampus_fcuser',
            },
        ),
    ]
