from django.shortcuts import render
from . import forms

# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()

    #Отправляем данные на фронт
    context = {'form': search_bar}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')
