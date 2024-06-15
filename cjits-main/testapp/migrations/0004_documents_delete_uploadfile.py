# Generated by Django 4.1.7 on 2023-04-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_alter_uploadfile_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('Class', models.CharField(max_length=30)),
                ('semister', models.CharField(max_length=30)),
                ('subject_name', models.CharField(max_length=50)),
                ('lecturename', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='uploadfile',
        ),
    ]
