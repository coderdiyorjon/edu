# Generated by Django 4.2 on 2024-10-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classes',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='science',
            options={'verbose_name': 'Science', 'verbose_name_plural': 'Sciences'},
        ),
        migrations.AlterField(
            model_name='classes',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='lessonName',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='pdfFile',
            field=models.FileField(upload_to='pdfFilesSchool'),
        ),
        migrations.AlterField(
            model_name='science',
            name='scienceName',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
