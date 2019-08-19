# Generated by Django 2.2.4 on 2019-08-19 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('from_hour', models.CharField(choices=[('8', '8'), ('9', '9'), ('9.30', '9.30'), ('10', '10'), ('10.30', '10.30'), ('11', '11'), ('11.30', '11.30'), ('12', '12'), ('12.30', '12.30'), ('13', '13'), ('13.30', '13.30'), ('14', '14'), ('14.30', '14.30'), ('15', '15'), ('15.30', '15.30'), ('16', '16'), ('16.30', '16.30'), ('17', '17'), ('17.30', '17.30'), ('18', '18'), ('18.30', '18.30'), ('19', '19'), ('19.30', '19.30'), ('20', '20')], max_length=5)),
                ('to_hour', models.CharField(choices=[('8', '8'), ('9', '9'), ('9.30', '9.30'), ('10', '10'), ('10.30', '10.30'), ('11', '11'), ('11.30', '11.30'), ('12', '12'), ('12.30', '12.30'), ('13', '13'), ('13.30', '13.30'), ('14', '14'), ('14.30', '14.30'), ('15', '15'), ('15.30', '15.30'), ('16', '16'), ('16.30', '16.30'), ('17', '17'), ('17.30', '17.30'), ('18', '18'), ('18.30', '18.30'), ('19', '19'), ('19.30', '19.30'), ('20', '20')], max_length=5)),
                ('location', models.CharField(choices=[('main hall', 'main hall'), ('class 201', 'class 201'), ('class 202', 'class 202'), ('class 203', 'class 203'), ('class 204', 'class 204'), ('class 205', 'class 205')], max_length=50)),
                ('instructor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FinalSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('schedule', models.ManyToManyField(to='schedule.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]