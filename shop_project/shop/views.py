from django.shortcuts import render
from .models import Product, Category, Order

def build_template(lst,cols):
    return [lst[i:i + cols] for i in range(0,len(lst),cols)]

def product_list(request):
    search_querry = request.GET.get("search", None)
    if search_querry:
        products = Product.objects.filter(title__icontains=search_querry)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/product_list.html', context={'product_list': build_template(products, 3), 'categories': categories})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories_list.html', context={'categories_list': categories})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    categories = Category.objects.all()
    return render(
        request, 'shop/product_detail.html', 
        context={'product': product, 'categories': categories})


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    categories = Category.objects.all()
    products = category.products.all()
    return render(
        request, 'shop/category_detail.html', 
        context={'category': category, 'categories': categories,
                 'product_list': build_template(products, 3)}
    )

def save_order(request):
    product = Product.objects.get(pk=request.POST['product_id'])
    order = Order()
    order.name = request.POST['username']
    order.email = request.POST['user_email']
    order.product = product
    order.save()
    categories = Category.objects.all()
    return render(request, 'shop/product_ordered.html',
    context={'product': product, 'categories': categories})
#нужно создать новую страницу вместо product_list.html