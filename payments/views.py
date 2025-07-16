from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PaymentForm

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirects to success page
    else:
        form = PaymentForm()
    return render(request, 'payments/payment_form.html', {'form': form})

# ✅ Add this view below the existing one
def success_view(request):
    return HttpResponse("Payment Successful!")
