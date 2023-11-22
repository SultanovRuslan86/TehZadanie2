from django.contrib import admin

# Register your models here.
from .models import Student, Semestr, StudentСard, SemestrCourse, Course, Teacher

admin.site.register(Student)
admin.site.register(Semestr)
admin.site.register(StudentСard)
admin.site.register(SemestrCourse)
admin.site.register(Course)
admin.site.register(Teacher)