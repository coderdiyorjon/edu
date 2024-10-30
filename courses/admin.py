from django.contrib import admin

# Register your models here.

from courses.models import Courses, Sciences, Lessons

# admin.site.register(Lessons)
# admin.site.register(Sciences)
# admin.site.register(Courses)

@admin.register(Courses)
class ClassesAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    ordering = ('-name',)

@admin.register(Sciences)
class SciencesAdmin(admin.ModelAdmin):
    list_display=('name', 'course',)
    search_fields=('name',)
    ordering = ('-name',)

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display=('name', 'time', 'science','course',)
    search_fields = ('name',)
    ordering = ('-name',)
    fields=['name','time', 'pdfFile', ('science','course')]