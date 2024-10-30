from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'

class SciencesUni(models.Model):
    name=models.CharField(max_length=100)
    course=models.ForeignKey(to=Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sciences'
        verbose_name = 'Science'

class LessonsUni(models.Model):
    name=models.CharField(max_length=100)
    time=models.PositiveIntegerField()
    pdfFile=models.FileField(upload_to='pdfFilesUniversity', null=True)
    course=models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    science=models.ForeignKey(to=SciencesUni, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Lesson'
        verbose_name_plural='Lessons'