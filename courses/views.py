# Create your views here.

from django.db.models import Q
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, render

from classes.models import Classes, SciencesSchool, LessonsSchool
from courses.models import Courses, SciencesUni, LessonsUni


def index(request):
    selected_science = request.GET.get('science')
    selected_course = request.GET.get('course')
    search_query = request.GET.get('page-header-search-input', '').strip()  # Get search input
    all_lessons_school = LessonsSchool.objects.all()
    all_lessons_uni = LessonsUni.objects.all()

    # Filter lessons based on search query, science, or course selection
    if search_query:
        lessons_school = all_lessons_school.filter(Q(lessonName__icontains=search_query))
        lessons_uni = all_lessons_uni.filter(Q(name__icontains=search_query))
    else:
        lessons_school = all_lessons_school
        lessons_uni = all_lessons_uni

    # Handle filtering based on selected science
    if selected_science:
        lessons_school = LessonsSchool.objects.filter(science__scienceName=selected_science)

    # Handle filtering based on selected course
    if selected_course:
        lessons_uni = LessonsUni.objects.filter(science__name=selected_course)

    context = {'title': "Javlon Domla Zo'r", 'classesSchool': Classes.objects.all(),
               'coursesSchool': Courses.objects.all(), 'SciencesSchoolwithNamesClasses': list(
            zip([str(name.classes) for name in SciencesSchool.objects.all()],
                [science.scienceName for science in SciencesSchool.objects.all()])),
               'SciencesUniwithNamesCourses': list(zip([str(name.course) for name in SciencesUni.objects.all()],
                                                       [science.name for science in SciencesUni.objects.all()])),
               'Lessonschool': lessons_school, 'Lessonsuni': lessons_uni, 'selected_science': selected_science,
               'selected_course': selected_course, 'search_query': search_query, }

    return render(request, 'index.html', context)


def download_pdf(request, lesson_id, model_type):
    if model_type == "school":
        lesson = get_object_or_404(LessonsSchool, id=lesson_id)
    elif model_type == "uni":
        lesson = get_object_or_404(LessonsUni, id=lesson_id)
    else:
        return HttpResponse("Invalid lesson type", status=400)

    response = FileResponse(lesson.pdfFile.open('rb'), as_attachment=True, filename=lesson.pdfFile.name)
    return response


def csrf_failure(request, reason=""):
    return render(request, "csrf_failure.html", {"reason": reason})
