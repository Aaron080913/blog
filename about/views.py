from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
# Create your views here.

def about_me(request):
    about = About.objects.all().order_by('updated_on').first()
    Collaborate_form = CollaborateForm()

    return render(request, 'about/about.html',
    {
        'about': about,
        'collaborate_form': Collaborate_form
    },
    )