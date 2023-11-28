from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from main.models import Information


# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')

        add_data = Information(name = name, age = age, email = email, password = password)
        add_data.save()

    form = Information.objects.all()

    return render (request, 'main/home.html', {'data': form})

def update(request, id):
    form = get_object_or_404(Information, pk=id)

    if request.method == 'POST':
        form.name = request.POST.get('name')
        form.age = request.POST.get('age')
        form.email = request.POST.get('email')
        form.password = request.POST.get('password')

        form.save()
        
    return render(request, 'main/update.html', {'data': form})

def delete(request, id):
    form = get_object_or_404(Information, pk=id)
    if request.method == 'POST':
        form.delete()
        return HttpResponseRedirect('/')
    
