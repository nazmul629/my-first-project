# Generated by Django 2.1.1 on 2018-09-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('roll', models.IntegerField()),
                ('bord', models.CharField(choices=[('d', 'Dhaka'), ('j', 'Jessor'), ('c', 'Comilla')], max_length=13)),
                ('school', models.CharField(max_length=40)),
                ('gpa', models.IntegerField()),
            ],
        ),
    ]
