# Generated by Django 2.2.2 on 2019-06-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('loc', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
