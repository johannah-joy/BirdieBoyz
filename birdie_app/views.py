from django.shortcuts import render, redirect
from .models import Birdie
from .forms import BirdieForm
from django.views import generic

# Create your views here.

def home(request):
    group = Birdie.objects.count()
    # count = Birdie.objects.order_by('date')
    if request.method == 'POST':
        form = BirdieForm(request.POST)
        if form.is_valid(): 
            form.save()
            birdies = Birdie.objects.all()
            return render(request, 'data.html', {'birdies': birdies})
    else:
        form_class = BirdieForm
    return render(request, 'home.html', {'group': group, 'form': form_class,})

def data(request):
    # # creating new object or instance in the database
    player_input = request.POST.get('player')
    if player_input == None:
        stats = Birdie.objects.all()
        context = {'stats': stats}
        return render(request, 'data.html', context)
    else:
        date_input = request.POST.get('date')
        course_input = request.POST.get('course')
        hole_input = request.POST.get('hole')
        Birdie.objects.create(player=player_input, date=date_input, course=course_input, hole=hole_input)
        stats = Birdie.objects.all()
        context = {'stats': stats}
        return render(request, 'data.html', context)

def bryan(request):
    stats = Birdie.objects.filter(player='Bryan')
    bryancount = Birdie.objects.filter(player='Bryan').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'bryan.html', {'bryancount': bryancount, 'stats': stats})

def david(request):
    stats = Birdie.objects.filter(player='David')
    davidcount = Birdie.objects.filter(player='David').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'david.html', {'davidcount': davidcount, 'stats': stats})

def greg(request):
    stats = Birdie.objects.filter(player='Greg')
    gregcount = Birdie.objects.filter(player='Greg').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'greg.html', {'gregcount': gregcount, 'stats': stats})

def steve(request):
    stats = Birdie.objects.filter(player='Steve')
    stevecount = Birdie.objects.filter(player='Steve').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'steve.html', {'stevecount': stevecount, 'stats': stats})