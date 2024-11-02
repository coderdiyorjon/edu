from django.shortcuts import render

from courses.models import Courses, LessonsUni, SciencesUni
from classes.models import Classes, SciencesSchool, LessonsSchool

# Create your views here.

def index(request):

    context={
        'title':"Javlon Domla Zo'r",
        'classesSchool': Classes.objects.all(),
        'SciencesSchool': SciencesSchool.objects.all(),
        'Lessonschool': LessonsSchool.objects.all(),
        'SciencesSchoolwithNamesClasses': zip([str(name.classes) for name in SciencesSchool.objects.all()],SciencesSchool.objects.all()),

    }
    return render(request, 'index.html', context)