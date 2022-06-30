from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentForm
from .models import Post
from .forms import *
from django.shortcuts import HttpResponse, render
from django.core.mail import send_mail


# Create your views here.


def home(request):
    if request.method == 'POST':
        details = PostForm(request.POST)

        if details.is_valid():

            post = details.save(commit=False)
            post.save()

            return HttpResponse("data submitted successfully")

        else:

            return render(request, "homepage.html", {'form': details})
    else:

        form = PostForm(None)
        return render(request, 'homepage.html', {'form': form})


def mail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return HttpResponse('thanks')
        else:

            return render(request, "mail.html", {'form': form})

    else:
        form = ContactForm()

    return render(request, 'mail.html', {'form': form})
