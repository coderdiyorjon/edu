# Generated by Django 4.2 on 2024-10-29 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Sciences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
            ],
            options={
                'verbose_name': 'Science',
                'verbose_name_plural': 'Sciences',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.PositiveIntegerField()),
                ('pdffile', models.FileField(upload_to='pdfFilesUniversity')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
                ('science', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.sciences')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
    ]
