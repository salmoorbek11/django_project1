from django.shortcuts import render
from pages.models import Person
from django.http import HttpResponseRedirect

from pages.models import ToDo

def home_page(request):
    people = Person.objects.all()
    return render(request, "home.html", {"people": people})
    
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.save()
    return HttpResponseRedirect("/")

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')