from django.contrib import admin
from .models import Payment
import csv
from django.http import HttpResponse

@admin.action(description="Export selected payments to CSV")
def export_payments_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=payments.csv'
    writer = csv.writer(response)
    writer.writerow(['Student', 'Amount Paid', 'Due Amount', 'Mode', 'Date'])
    for p in queryset:
        writer.writerow([p.student.name, p.amount_paid, p.due_amount, p.payment_mode, p.payment_date])
    return response

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'amount_paid', 'due_amount', 'payment_mode', 'payment_date']
    search_fields = ['student__name']
    list_filter = ['payment_mode', 'payment_date']
    actions = [export_payments_csv]
