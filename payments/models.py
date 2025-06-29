from django.db import models
from students.models import Student

class Payment(models.Model):
    PAYMENT_MODES = [
        ('UPI', 'UPI'),
        ('CASH', 'Cash'),
        ('CARD', 'Card'),
        ('BANK', 'Bank Transfer'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    payment_date = models.DateField(auto_now_add=True)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODES)
    remarks = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # Automatically calculate due amount if not manually entered
        self.due_amount = self.total_fee - self.amount_paid
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - ₹{self.amount_paid} on {self.payment_date}"
