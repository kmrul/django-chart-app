from chartapp.form import ProductForm
from chartapp.models import Product
from django.shortcuts import redirect, render
from .form import ProductForm

def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()

    context = {
        "products": products,
        "form": form
    }

    return render(request, 'chartapp/index.html', context=context)