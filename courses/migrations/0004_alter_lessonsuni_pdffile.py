# Generated by Django 4.2 on 2024-11-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_lessonsuni_pdffile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonsuni',
            name='pdfFile',
            field=models.FileField(blank=True, null=True, upload_to='pdfFilesUniversity'),
        ),
    ]
