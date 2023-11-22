from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, filters
from rest_framework.response import Response
from myapp.models import *
from myapp.serializers import StudentSerializer, CourseSerializer, SemestrSerializer, SemestrCourseSerializer, TeacherSerializer, StudentCardSerializer

class StudentCardIdViewSet(viewsets.ModelViewSet):
    queryset = StudentСard.objects.all()
    serializer_class = StudentCardSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['stud_surname__startswith']

    # Пример тега фильтрации по первой букве фамилии,
    # адрес в браузере http://127.0.0.1:8000/students/?surname_start="введите первую букву фамилии"
    def get_queryset(self):
        queryset = super().get_queryset()

        surname_start = self.request.query_params.get('surname_start')

        if surname_start:
            queryset = queryset.filter(stud_surname__startswith=surname_start)

        return queryset


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    # фильтрация по номеру курса
    # адрес в браузере http://127.0.0.1:8000/courses/?search="введите номер курса"
    search_field = ['course_number']

class SemestrViewSet(viewsets.ModelViewSet):
    queryset = Semestr.objects.all()
    serializer_class = SemestrSerializer

class SemestrCourseViewSet(viewsets.ModelViewSet):
    queryset = SemestrCourse.objects.all()
    serializer_class = SemestrCourseSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['surname__startswith']

    # Пример тега фильтрации по первой букве фамилии преподавателя,
    # адрес в браузере http://127.0.0.1:8000/teachers/?surname_start="введите первую букву фамилии"
    def get_queryset(self):
        queryset = super().get_queryset()

        surname_start = self.request.query_params.get('surname_start')

        if surname_start:
            queryset = queryset.filter(surname__startswith=surname_start)

        return queryset