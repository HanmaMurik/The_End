from django.shortcuts import render, redirect
from . import forms, models


# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()

    #Отправляем данные на фронт
    context = {'form': search_bar,
               'products': products,
               'categories': categories}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def get_exact_category(request, pk):
    category = models.Category.objects.get(id=pk)
    products = models.Product.objects.filter(product_category=category)

    context = {'products': products}
    return render(request, 'exact_category.html', context)

def get_exact_product(request, pk):
    product = models.Product.objects.get(id=pk)

    context = {'product': product}
    return render(request, 'exact_product.html', context)

def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')

        try:
            exact_product = models.Product.objects.get(product_name__icontains=get_product)

            return redirect(f'product/{exact_product.id}')
        except:
            return redirect('/')







