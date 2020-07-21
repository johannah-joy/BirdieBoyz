from django.shortcuts import render, redirect
from .models import Birdie
from .forms import BirdieForm
from django.views import generic

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = BirdieForm(request.POST)
        if form.is_valid(): 
            form.save()
            birdies = Birdie.objects.all()
            return render(request, 'data.html', {'birdies': birdies})
    else:
        form_class = BirdieForm
    return render(request, 'home.html', {'form': form_class,})

def data(request):
    # # creating new object or instance in the database
    player_input = request.POST.get('player')
    # print(player_input, '38')
    date_input = request.POST.get('date')
    course_input = request.POST.get('course')
    hole_input = request.POST.get('hole')
    Birdie.objects.create(player=player_input, date=date_input, course=course_input, hole=hole_input)
    stats = Birdie.objects.all()
    # context = {'data': stats}
    context = {'stats': stats}
    return render(request, 'data.html', context)
    # return render(request, f'{player_input}.html', context)
    # else:
    #     stats = Birdie.objects.all()
    #     # context = {'data': stats}
    #     context = {'stats': stats}
    #     return render(request, 'data.html', context)

def bryan(request):
    stats = Birdie.objects.filter(player='Bryan')
    # context = {'data': stats}
    context = {'stats': stats}
    # return render(request, f'{player_input}.html', context)
    return render(request, 'bryan.html', context)

def david(request):
    stats = Birdie.objects.filter(player='David')
    # context = {'data': stats}
    context = {'stats': stats}
    # return render(request, f'{player_input}.html', context)
    return render(request, 'david.html', context)

def greg(request):
    stats = Birdie.objects.filter(player='Greg')
    # context = {'data': stats}
    context = {'stats': stats}
    # return render(request, f'{player_input}.html', context)
    return render(request, 'greg.html', context)

def steve(request):
    stats = Birdie.objects.filter(player='Steve')
    # context = {'data': stats}
    context = {'stats': stats}
    # return render(request, f'{player_input}.html', context)
    return render(request, 'steve.html', context)