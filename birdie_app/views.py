from django.shortcuts import render, redirect
from .models import Birdie
from .forms import BirdieForm
from django.views import generic

# Create your views here.

def home(request):
    # context = {} 
    # context['form'] = GeeksForm() 
    # return render( request, "home.html", context)

    # from .forms import GeeksForm 
  
    # # Create your views here. 
    # def home_view(request): 
    #     context ={} 
    #     form = GeeksForm() 
    #     context['form']= form 
    #     if request.GET: 
    #         temp = request.GET['geeks_field'] 
    #         print(temp) 
    #     return render(request, "home.html", context)

    if request.method == 'POST':
        form = BirdieForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            birdies = Birdie.objects.all()
            return render(request, '/data.html', {'birdies': birdies})
    else:
        form_class = BirdieForm
    return render(request, "/home.html", {
        'form': form_class,})

def data(request):
    # if form submitted:
        player_input = request.POST.get('player')
        date_input = request.POST.get('date')
        course_input = request.POST.get('course')
        hole_input = request.POST.get('hole')
        Birdie.objects.create(player=player_input, date=date_input, course=course_input, hole=hole_input)
        stats = Birdie.objects.all()
        # context = {'data': stats}
        context = {'stats': stats}
        return render(request, '/data.html', context)
    # else:
    #     stats = Birdie.objects.all()
    #     # context = {'data': stats}
    #     context = {'stats': stats}
    #     return render(request, 'data.html', context)

class BryanView(generic.TemplateView):
    # model = Birdie
    # form_class = 
    template_name = 'bryan.html'
    # success_url = reverse_lazy('home')

class DavidView(generic.TemplateView):
    template_name = 'david.html'

class GregView(generic.TemplateView):
    template_name = 'greg.html'

class SteveView(generic.TemplateView):
    template_name = 'steve.html'