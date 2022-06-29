from django.shortcuts import render
from .forms import StudentForm
from .models import Post
from .forms import PostForm
from django.shortcuts import HttpResponse, render

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
