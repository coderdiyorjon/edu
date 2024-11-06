# Generated by Django 4.2 on 2024-10-30 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonsUni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.PositiveIntegerField()),
                ('pdfFile', models.FileField(upload_to='pdfFilesUniversity')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.RenameModel(
            old_name='Sciences',
            new_name='SciencesUni',
        ),
        migrations.DeleteModel(
            name='Lessons',
        ),
        migrations.AddField(
            model_name='lessonsuni',
            name='science',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.sciencesuni'),
        ),
    ]
