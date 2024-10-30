from django.shortcuts import render

from courses.models import Courses, LessonsUni, SciencesUni
from classes.models import Classes, SciencesSchool, LessonsSchool

# Create your views here.

def index(request):

    # ''' sciencesCourse massivi '''

    sciences_list=[str(item.course) for item in SciencesUni.objects.all()]
    context={
        'title':'Javlon Domla Zo\'r',
        'coursesUni': Courses.objects.all(),
        'lessonsUni': LessonsUni.objects.all(),
        'sciencesUni': SciencesUni.objects.all(),
        'classesSchool': Classes.objects.all(),
        'lessonsSchool': LessonsSchool.objects.all(),
        'sciencesSchool': SciencesSchool.objects.all(),
        # 'scienceStrUni': sciencestruni,
        'sciences_list':zip(sciences_list,SciencesUni.objects.all())
    }
    return render(request, 'index.html', context)