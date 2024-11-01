from django.contrib import admin

from classes.models import Classes, SciencesSchool, LessonsSchool

# Register your models here.

@admin.register(Classes)
class ClassesSchoolAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    ordering = ('-name',)

@admin.register(SciencesSchool)
class SciencesSchoolAdmin(admin.ModelAdmin):
    list_display=('scienceName', 'classes',)
    search_fields=('scienceName',)
    ordering = ('-scienceName',)

@admin.register(LessonsSchool)
class LessonsSchoolAdmin(admin.ModelAdmin):
    list_display=('lessonName', 'time', 'science','classes',)
    search_fields = ('lessonName',)
    ordering = ('-lessonName',)
    fields=['lessonName','time', 'pdfFile', ('science','classes')]

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "classes" and "science" in request.GET:
    #         science_id = request.GET.get('science')
    #         kwargs["queryset"] = Classes.objects.filter(sciencesschool__id=science_id)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

# admin.site.register(Classes)
# admin.site.register(SciencesSchool)
# admin.site.register(LessonsSchool, LessonsSchoolAdmin)