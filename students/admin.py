# students/admin.py
from django.contrib import admin
from .models import Student
from attendance.models import Attendance
from datetime import date

@admin.action(description="Mark selected students Present for today")
def mark_present(modeladmin, request, queryset):
    today = date.today()
    for student in queryset:
        Attendance.objects.get_or_create(student=student, date=today, defaults={'status': 'Present'})

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'enrollment_number']
    actions = [mark_present]
