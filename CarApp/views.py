from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, Product
from .forms import ProductForm
from .forms import Signupform


# Create your views here.

def categories(request):
    categories = Category.objects.filter().all()
    context = {'kategorie': categories}
    return render(request, 'categories.html', context=context)


def home(request):
    context = {}
    return render(request, 'home.html', context=context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context=context)


@login_required(login_url='login')
def tires(request):
    if not request.user.is_authenticated:
        messages.error(request, "Log in to your account.")
        return redirect('login')
    tires_categories = Category.objects.filter(name='Tires')
    products = Product.objects.filter(category__in=tires_categories)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')

    context = {"products": page_obj}
    return render(request, 'Tires.html', context=context)


@login_required(login_url='login')
def batteries(request):
    if not request.user.is_authenticated:
        messages.error(request, "Log in to your account.")
        return redirect('login')
    batteries = Category.objects.filter(name='Batteries')
    products = Product.objects.filter(category__in=batteries)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')

    context = {"products": page_obj}
    return render(request, 'Batteries.html', context=context)


@login_required(login_url='login')
def maintenance(request):
    if not request.user.is_authenticated:
        messages.error(request, "Log in to your account.")
        return redirect('login')
    care = Category.objects.filter(name='Maintenance')
    products = Product.objects.filter(category__in=care)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')

    context = {"products": page_obj}
    return render(request, 'Maintenance.html', context=context)


@login_required(login_url='login')
def clothing(request):
    if not request.user.is_authenticated:
        messages.error(request, "Log in to your account.")
        return redirect('login')
    clothes = Category.objects.filter(name='Clothing')
    products = Product.objects.filter(category__in=clothes)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')

    context = {"products": page_obj}
    return render(request, 'Clothing.html', context=context)


@login_required(login_url='login')
def helmets(request):
    if not request.user.is_authenticated:
        messages.error(request, "Log in to your account.")
        return redirect('login')
    hel = Category.objects.filter(name='Helmets')
    products = Product.objects.filter(category__in=hel)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')

    context = {"products": page_obj}
    return render(request, 'Helmets.html', context=context)


# @login_required(login_url='login')
def motoroil(request):
    oil = Category.objects.filter(name='Motor-Oil')
    products = Product.objects.filter(category__in=oil)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Log in to your account.")
            return redirect('login')
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')

    context = {"products": page_obj}
    return render(request, 'Motor-Oil.html', context=context)


@login_required(login_url='login')
def cart(request):
    if not request.user.is_authenticated:
        messages.error(request, "Log in to your account.")
        return redirect('login')

    user_cart = Cart.objects.filter(user=request.user)
    context = {"cart": user_cart}
    return render(request, 'cart.html', context=context)


def delete_item(request, item_id):
    cart_item = Cart.objects.get(pk=item_id)
    cart_item.delete()
    return redirect('cart')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def upload(request):
    if request.method == "POST":
        form_data = ProductForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            form_data.save()  # Save the form data to create a new product
            messages.success(request, "Product is added.")
            return redirect('upload')

    context = {"form": ProductForm}
    return render(request, 'upload.html', context=context)


def signup(request):
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Signupform()
    return render(request, 'signup.html', {'form': form})


def payment(request):

    user_cart = Cart.objects.filter(user=request.user)
    context = {"cart": user_cart}
    return render(request, 'payment.html', context=context)
