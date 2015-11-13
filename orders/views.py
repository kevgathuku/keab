from django.shortcuts import render
from .forms import OrderForm

# Create your views here.
def order_new(request):
    form = OrderForm()
    return render(request, 'orders.html', {'form': form})