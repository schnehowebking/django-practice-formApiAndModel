from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def contact_form(request):
    form = ContactForm()
    return render(request, './formapi/form.html', {'form':form})


def contact_form_view(request):
    form = ContactForm()
    pass
