from django.http import JsonResponse
from .models import Student

def student_list(request):
    students = Student.objects.all().values('id', 'name', 'email', 'dob', 'joined_on')
    return JsonResponse(list(students), safe=False)
