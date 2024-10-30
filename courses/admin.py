from django.contrib import admin

# Register your models here.

from courses.models import Courses, SciencesUni, LessonsUni

# admin.site.register(Lessons)
# admin.site.register(Sciences)
# admin.site.register(Courses)

@admin.register(Courses)
class ClassesUniAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    ordering = ('-name',)

@admin.register(SciencesUni)
class SciencesUniAdmin(admin.ModelAdmin):
    list_display=('name', 'course',)
    search_fields=('name',)
    ordering = ('-name',)

@admin.register(LessonsUni)
class LessonsUniAdmin(admin.ModelAdmin):
    list_display=('name', 'time', 'science','course',)
    search_fields = ('name',)
    ordering = ('-name',)
    fields=['name','time', 'pdfFile', ('science','course')]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "course":
            # GET orqali tanlangan fan ID sini tekshirish
            if 'science' in request.GET:
                try:
                    science_id = int(request.GET.get('science'))
                    kwargs["queryset"] = Courses.objects.filter(sciencesuni__id=science_id)
                except (ValueError, TypeError):
                    pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)