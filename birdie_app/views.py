from django.shortcuts import render, redirect
from .models import Birdie
from .forms import BirdieForm
from django.views import generic

# Create your views here.

def home(request):
    # group2021 = Birdie.objects.count()
    group2021 = Birdie.objects.filter(date__year='2021').count()
    group2020 = Birdie.objects.filter(date__year='2020').count()
    if request.method == 'POST':
        form = BirdieForm(request.POST)
        if form.is_valid(): 
            form.save()
            birdies = Birdie.objects.all()
            return render(request, 'data.html', {'birdies': birdies})
    else:
        form_class = BirdieForm
    return render(request, 'home.html', {'group2021': group2021, 'group2020': group2020, 'form': form_class,})

def data(request):
    # # creating new object or instance in the database
    player_input = request.POST.get('player')
    if player_input == None:
        stats = Birdie.objects.all().order_by('-date', '-hole')
        context = {'stats': stats}
        return render(request, 'data.html', context)
    else:
        date_input = request.POST.get('date')
        course_input = request.POST.get('course')
        hole_input = request.POST.get('hole')
        Birdie.objects.create(player=player_input, date=date_input, course=course_input, hole=hole_input)
        stats = Birdie.objects.all().order_by('-date', '-hole')
        context = {'stats': stats}
        return render(request, 'data.html', context)

def bryan(request):
    stats = Birdie.objects.filter(player='Bryan').order_by('-date', '-hole')
    bryancount2021 = Birdie.objects.filter(player='Bryan', date__year='2021').count()
    bryancount2020 = Birdie.objects.filter(player='Bryan', date__year='2020').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'bryan.html', {'bryancount2021': bryancount2021, 'bryancount2020': bryancount2020, 'stats': stats})

def david(request):
    stats = Birdie.objects.filter(player='David').order_by('-date', '-hole')
    davidcount2021 = Birdie.objects.filter(player='David', date__year='2021').count()
    davidcount2020 = Birdie.objects.filter(player='David', date__year='2020').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'david.html', {'davidcount2021': davidcount2021, 'davidcount2020': davidcount2020, 'stats': stats})

def greg(request):
    stats = Birdie.objects.filter(player='Greg').order_by('-date', '-hole')
    gregcount2021 = Birdie.objects.filter(player='Greg', date__year='2021').count()
    gregcount2020 = Birdie.objects.filter(player='Greg', date__year='2020').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'greg.html', {'gregcount2021': gregcount2021, 'gregcount2020': gregcount2020, 'stats': stats})

def steve(request):
    stats = Birdie.objects.filter(player='Steve').order_by('-date', '-hole')
    stevecount2021 = Birdie.objects.filter(player='Steve', date__year='2021').count()
    stevecount2020 = Birdie.objects.filter(player='Steve', date__year='2020').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'steve.html', {'stevecount2021': stevecount2021, 'stevecount2020': stevecount2020, 'stats': stats})