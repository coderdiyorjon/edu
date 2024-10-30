from django.db import models

# Create your models here.

class Classes(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Classes'
        verbose_name = 'Class'

class Science(models.Model):
    scienceName = models.CharField(max_length=100)
    classes = models.ForeignKey(to=Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.scienceName

    class Meta:
        verbose_name_plural='Sciences'
        verbose_name='Science'

class Lessons(models.Model):
    lessonName = models.CharField(max_length=100)
    time=models.PositiveSmallIntegerField()
    pdfFile=models.FileField(upload_to='pdfFilesSchool')
    classes = models.ForeignKey(to=Classes, on_delete=models.CASCADE)
    science=models.ForeignKey(to=Science,on_delete=models.CASCADE)

    def __str__(self):
        return self.lessonName

    class Meta:
        verbose_name_plural = 'Lessons'
        verbose_name = 'Lesson'