from django.contrib import admin
from .models import Exam, ExamResult
import csv
from django.http import HttpResponse

@admin.action(description="Export selected exams to CSV")
def export_exam_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=exams.csv'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Course', 'Date'])
    for exam in queryset:
        writer.writerow([exam.name, exam.course.name, exam.exam_date])
    return response

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'exam_date']
    search_fields = ['name', 'course__name']
    list_filter = ['exam_date']
    actions = [export_exam_csv]

@admin.action(description="Export selected results to CSV")
def export_results_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=exam_results.csv'
    writer = csv.writer(response)
    writer.writerow(['Student', 'Exam', 'Marks'])
    for result in queryset:
        writer.writerow([result.student.name, result.exam.name, result.marks_obtained])
    return response

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'marks_obtained']
    search_fields = ['student__name', 'exam__name']
    list_filter = ['exam']
    actions = [export_results_csv]
