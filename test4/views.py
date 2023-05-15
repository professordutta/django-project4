from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

def contact(request):
    form  = ContactForm
    return render(request, 'test4/contact.html', {'form': form})

def add_record(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Data Added Successfully</h2>')
