from django.db import models
from students.models import Student
import qrcode
from io import BytesIO
from django.core.files import File

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
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=20, blank=True, null=True)
    card_holder_name = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.CharField(max_length=7, blank=True, null=True) 
    
    def generate_qr_code(self):
        data = f"upi://pay?pa=your-upi-id@bank&pn=ERPSystem&am={self.amount_paid}&cu=INR"
        qr = qrcode.make(data)
        blob = BytesIO()
        qr.save(blob, format='PNG')
        self.qr_code.save(f'payment_qr_{self.id}.png', File(blob), save=False)

    def save(self, *args, **kwargs):
        self.due_amount = self.total_fee - self.amount_paid
        super().save(*args, **kwargs)

        if not self.qr_code:
            self.generate_qr_code()
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - ₹{self.amount_paid} on {self.payment_date}"


