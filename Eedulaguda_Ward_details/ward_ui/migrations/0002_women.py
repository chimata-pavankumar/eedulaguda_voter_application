# Generated by Django 2.0.7 on 2020-01-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ward_ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='women',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('husband_name', models.CharField(default='not entered', max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('door_no', models.CharField(default='not provided', max_length=200)),
                ('age', models.CharField(max_length=200)),
            ],
        ),
    ]
