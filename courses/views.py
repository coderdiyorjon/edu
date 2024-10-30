from django.shortcuts import render

from courses.models import Courses, Lessons, Sciences
from classes.models import Classes, Science, Lessons

# Create your views here.

def index(request):
    sciencestruni=[str(item.course) for item in Sciences.objects.all()]
    context={
        'title':'Javlon Domla Zo\'r',
        'coursesUni': Courses.objects.all(),
        'lessonsUni': Lessons.objects.all(),
        'sciencesUni': Sciences.objects.all(),
        'classesSchool': Classes.objects.all(),
        'lessonsSchool': Lessons.objects.all(),
        'sciencesSchool': Science.objects.all(),
        # 'scienceStrUni': sciencestruni,
        'sciences_list':zip(sciencestruni,Sciences.objects.all())
    }
    return render(request, 'index.html', context)