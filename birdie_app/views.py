from django.shortcuts import render, redirect
from .models import Birdie
from .forms import BirdieForm
from django.views import generic

# Create your views here.

def home(request):
    # group2021 = Birdie.objects.count()
    group2023 = Birdie.objects.filter(date__year='2023').count()
    group2022 = Birdie.objects.filter(date__year='2022').count()
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
    return render(request, 'home.html', {'group2023': group2023, 'group2022': group2022, 'group2021': group2021, 'group2020': group2020, 'form': form_class,})

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
    bryancount2023 = Birdie.objects.filter(player='Bryan', date__year='2023').count()
    bryancount2022 = Birdie.objects.filter(player='Bryan', date__year='2022').count()
    bryancount2021 = Birdie.objects.filter(player='Bryan', date__year='2021').count()
    bryancount2020 = Birdie.objects.filter(player='Bryan', date__year='2020').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'bryan.html', {'bryancount2023': bryancount2023, 'bryancount2022': bryancount2022, 'bryancount2021': bryancount2021, 'bryancount2020': bryancount2020, 'stats': stats})

def david(request):
    stats = Birdie.objects.filter(player='David').order_by('-date', '-hole')
    davidcount2023 = Birdie.objects.filter(player='David', date__year='2023').count()
    davidcount2022 = Birdie.objects.filter(player='David', date__year='2022').count()
    davidcount2021 = Birdie.objects.filter(player='David', date__year='2021').count()
    davidcount2020 = Birdie.objects.filter(player='David', date__year='2020').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'david.html', {'davidcount2023': davidcount2023, 'davidcount2022': davidcount2022, 'davidcount2021': davidcount2021, 'davidcount2020': davidcount2020, 'stats': stats})

def greg(request):
    stats = Birdie.objects.filter(player='Greg').order_by('-date', '-hole')
    gregcount2023 = Birdie.objects.filter(player='Greg', date__year='2023').count()
    gregcount2022 = Birdie.objects.filter(player='Greg', date__year='2022').count()
    gregcount2021 = Birdie.objects.filter(player='Greg', date__year='2021').count()
    gregcount2020 = Birdie.objects.filter(player='Greg', date__year='2020').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'greg.html', {'gregcount2023': gregcount2023, 'gregcount2022': gregcount2022, 'gregcount2021': gregcount2021, 'gregcount2020': gregcount2020, 'stats': stats})

def kara(request):
    stats = Birdie.objects.filter(player='Kara').order_by('-date', '-hole')
    karacount2023 = Birdie.objects.filter(player='Kara', date__year='2023').count()
    karacount2022 = Birdie.objects.filter(player='Kara', date__year='2022').count()
    return render(request, 'kara.html', {'karacount2023': karacount2023, 'karacount2022': karacount2022, 'stats': stats})

def steve(request):
    stats = Birdie.objects.filter(player='Steve').order_by('-date', '-hole')
    stevecount2023 = Birdie.objects.filter(player='Steve', date__year='2023').count()
    stevecount2022 = Birdie.objects.filter(player='Steve', date__year='2022').count()
    stevecount2021 = Birdie.objects.filter(player='Steve', date__year='2021').count()
    stevecount2020 = Birdie.objects.filter(player='Steve', date__year='2020').count()
    # return render(request, f'{player_input}.html', context)
    return render(request, 'steve.html', {'stevecount2023': stevecount2023, 'stevecount2022': stevecount2022, 'stevecount2021': stevecount2021, 'stevecount2020': stevecount2020, 'stats': stats})