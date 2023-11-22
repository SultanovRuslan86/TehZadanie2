from drf_spectacular.utils import extend_schema, OpenApiParameter
from myapp.models import Student
from myapp.serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
@extend_schema(
    summary='Get all students',
    responses={200: StudentSerializer(many=True)},
)
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@extend_schema(
    summary='Create a student',
    request=StudentSerializer,
    responses={201: StudentSerializer},
)
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@extend_schema(
    summary='Delete a student',
)
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'PATCH'])
@extend_schema(
    summary='Update a student',
    request=StudentSerializer,
    responses={200: StudentSerializer},
)
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)