# Generated by Django 2.2.5 on 2019-12-05 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
                ('city', models.TextField()),
                ('street', models.TextField()),
                ('building_number', models.IntegerField()),
                ('postal_code', models.IntegerField()),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id_number', models.TextField()),
                ('specialty', models.TextField()),
                ('group', models.TextField()),
                ('semester', models.IntegerField()),
                ('training_form', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('phone', models.TextField()),
                ('age', models.IntegerField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to='api.Address')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('rating', models.FloatField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='university', to='api.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.TextField()),
                ('salary', models.IntegerField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='api.University')),
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='api.Address')),
            ],
        ),
        migrations.CreateModel(
            name='StudentPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.TextField()),
                ('date', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_performance', to='api.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_performance', to='api.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='api.University'),
        ),
        migrations.AddField(
            model_name='student',
            name='user_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='api.Address'),
        ),
    ]