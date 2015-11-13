from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import OrderForm


def order_new(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Order Succesfully Saved')
            return HttpResponseRedirect('/order/new')
        else:
            form = OrderForm()
            messages.add_message(request, messages.ERROR,
                                 'Ooops, an Error Occurred!')
            return render(request, 'orders.html', {'form': form})
    else:
        form = OrderForm()
        return render(request, 'orders.html', {'form': form})
