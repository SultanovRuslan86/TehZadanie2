from datetime import date
from django_seed import Seed
from models import Student, Semestr, StudentСard, SemestrCourse, Course, Teacher

import os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_tz.settings")
settings.configure()

def run():
    seeder = Seed.seeder()

    seeder.add_entity(StudentСard, 10, {
        'student_id': lambda x: random.randint(1000, 9999),
        'student_name': lambda x: seeder.faker.name(),
    })

    students = seeder.execute()
    for student in students[StudentСard]:
        seeder.add_entity(Student, 5, {
            'student_card': student,
            'stud_name': lambda x: seeder.faker.first_name(),
            'stud_surname': lambda x: seeder.faker.last_name(),
        })

    courses = seeder.execute()
    for student in students[Student]:
        seeder.add_entity(Course, 3, {
            'course_id': student,
            'course_name': lambda x: seeder.faker.catch_phrase(),
            'course_number': lambda x: random.randint(1, 10),
        })

    semestr_courses = seeder.execute()
    for course in courses[Course]:
        seeder.add_entity(SemestrCourse, 2, {
            'course': course,
            'semestr_number': lambda x: random.randint(1, 3),
            'start_date': lambda x: seeder.faker.date_between(start_date='-30d', end_date='today'),
            'end_date': lambda x: seeder.faker.date_between(start_date='today', end_date='+30d'),
        })

    semestrs = seeder.execute()
    for semestr_course in semestr_courses[SemestrCourse]:
        seeder.add_entity(Semestr, 1, {
            'semestr_id': semestr_course,
            'semestr_num': lambda x: random.randint(1, 10),
        })

    teachers = seeder.execute()
    for semestr in semestrs[Semestr]:
        seeder.add_entity(Teacher, 3, {
            'teacher_id': semestr,
            'name': lambda x: seeder.faker.first_name(),
            'surname': lambda x: seeder.faker.last_name(),
        })

run()

# Для запуска используем команду - python seeds.py , находясь в той же дирректории


