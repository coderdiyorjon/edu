from django.contrib import admin

from classes.models import Classes, Science, Lessons

# Register your models here.

# admin.site.register(Lessons)
# admin.site.register(Science)
# admin.site.register(Classes)

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    ordering = ('-name',)

@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display=('scienceName', 'classes',)
    search_fields=('scienceName',)
    ordering = ('-scienceName',)

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display=('lessonName', 'time', 'science','classes',)
    search_fields = ('lessonName',)
    ordering = ('-lessonName',)
    fields=['lessonName','time', 'pdfFile', ('science','classes')]