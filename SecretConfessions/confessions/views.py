from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Confession

def home_secret(request):
    confessions = Confession.objects.all().order_by('-date_posted')
    return render(request, 'confessions/secret.html', {'confessions': confessions})

def home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Confession.objects.create(content=content)
            return redirect('thank_you')
    return render(request, 'confessions/home.html')

def thank_you(request):
    return render(request, 'confessions/thank_you.html')
