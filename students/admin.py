from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'dob', 'joined_on']
    search_fields = ['name', 'email']
    list_filter = ['joined_on', 'dob']

