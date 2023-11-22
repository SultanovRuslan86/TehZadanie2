from rest_framework import serializers
from .models import *

class StudentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentСard
        fields = ['student_id', 'student_name']


class StudentSerializer(serializers.ModelSerializer):
    student_card = StudentCardSerializer()  # Вложенный сериализатор

    class Meta:
        model = Student
        fields = ['id', 'stud_name', 'stud_surname', 'student_card']

    def create(self, validated_data):
        student_card_data = validated_data.pop('student_card')
        student_card = StudentСard.objects.create(**student_card_data)
        student = Student.objects.create(student_card=student_card, **validated_data)
        return student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'course_number']


class SemestrCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemestrCourse
        fields = ['course', 'semestr_number', 'start_date', 'end_date']


class SemestrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestr
        fields = ['semestr_id', 'semestr_num']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'surname', 'name']
