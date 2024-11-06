# Create your views here.

from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, render

from classes.models import Classes, SciencesSchool, LessonsSchool
from courses.models import Courses, SciencesUni, LessonsUni

import fitz
import re


def qidirish_pdfs(pdf_files, search_query):
    matched_lessons = []

    for lesson in pdf_files:
        # Ensure PDF file exists and is accessible
        if lesson.pdfFile:
            pdf_path = lesson.pdfFile.path  # Full path of the PDF file

            try:
                # Open and read the PDF file
                with fitz.open(pdf_path) as pdf:
                    # Iterate through each page
                    for page_num in range(pdf.page_count):
                        page = pdf[page_num]
                        text = page.get_text()

                        # Check if search_query is in this page
                        if search_query.lower() in text.lower():
                            matched_lessons.append(lesson)
                            break  # Stop if match is found in the current PDF

            except Exception as e:
                print(f"Error reading PDF {pdf_path}: {e}")

    return matched_lessons


from django.shortcuts import render
from classes.models import LessonsSchool
from courses.models import LessonsUni

def index(request):
    search_query = request.GET.get('page-header-search-input', '').strip()  # Get the search input
    selected_science = request.GET.get('science')
    selected_course = request.GET.get('course')

    # Get all lessons
    lessons_school = LessonsSchool.objects.all()
    lessons_uni = LessonsUni.objects.all()

    # If there is a search query, filter lessons by PDF content
    if search_query:
        lessons_school = qidirish_pdfs(lessons_school, search_query)
        lessons_uni = qidirish_pdfs(lessons_uni, search_query)
    else:
        # Filter by science or course if selected
        if selected_science:
            lessons_school = lessons_school.filter(science__scienceName=selected_science)
            lessons_uni = None
        elif selected_course:
            lessons_uni = lessons_uni.filter(science__name=selected_course)
            lessons_school = None

    context = {
        'title': "Javlon Domla Zo'r",
        'classesSchool': Classes.objects.all(),
        'coursesSchool': Courses.objects.all(),
        'SciencesSchoolwithNamesClasses': list(zip(
            [str(name.classes) for name in SciencesSchool.objects.all()],
            [science.scienceName for science in SciencesSchool.objects.all()]
        )),
        'SciencesUniwithNamesCourses': list(zip(
            [str(name.course) for name in SciencesUni.objects.all()],
            [science.name for science in SciencesUni.objects.all()]
        )),
        'Lessonschool': lessons_school,
        'Lessonsuni': lessons_uni,
        'selected_science': selected_science,
        'selected_course': selected_course,
        'search_query': search_query,
    }
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
