# Generated by Django 2.2.5 on 2019-12-05 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='address',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
        migrations.AlterModelTable(
            name='studentperformance',
            table='student_performance',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teacher',
        ),
        migrations.AlterModelTable(
            name='university',
            table='university',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='user_info',
        ),
    ]
