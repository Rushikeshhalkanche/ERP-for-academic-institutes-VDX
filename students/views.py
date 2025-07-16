from django.http import JsonResponse
from .models import Student

def student_list(request):
    students = Student.objects.all().values(
        'id',
        'name',
        'email',
        'dob',
        'joined_on',
        'enrollment_number',  # ✅ New field
        'phone_number',       # 🆕 You can include this if added
        'address'             # 🆕 Include any other fields
    )
    return JsonResponse(list(students), safe=False)

