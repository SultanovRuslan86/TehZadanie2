from django.db import models

class StudentСard(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name

class Student(models.Model):
    student_card = models.ForeignKey(StudentСard, on_delete=models.CASCADE)
    stud_name = models.CharField(max_length=50)
    stud_surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.stud_surname} {self.stud_name}'

class Course(models.Model):
    course_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=300)
    course_number = models.IntegerField()

    def __str__(self):
        return self.course_name

class SemestrCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semestr_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.semestr_number)


class Semestr(models.Model):
    semestr_id = models.ForeignKey(SemestrCourse, on_delete=models.CASCADE)
    semestr_num = models.IntegerField()

    def __str__(self):
        return str(self.semestr_num)

class Teacher(models.Model):
    teacher_id = models.ForeignKey(Semestr, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.surname} {self.name}'



