from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Category, MenuItem
from .forms import MenuItemForm, CategoryForm


def menu_view(request):
    search_query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '')

    categories = Category.objects.all()
    items = MenuItem.objects.select_related('category').order_by('category__name', 'name')

    if search_query:
        items = items.filter(name__icontains=search_query) | items.filter(description__icontains=search_query)
        items = items.order_by('category__name', 'name')

    if category_id:
        items = items.filter(category__id=category_id)

    context = {
        'categories': categories,
        'items': items,
        'search_query': search_query,
        'active_category': category_id,
    }
    return render(request, 'menu/menu.html', context)

# --- Dashboard Views ---

def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('menu:dashboard_home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu:dashboard_home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})

def dashboard_logout(request):
    logout(request)
    return redirect('menu:dashboard_login')

@login_required(login_url='menu:dashboard_login')
def dashboard_home(request):
    categories = Category.objects.all()
    items = MenuItem.objects.all().order_by('-created_at')
    return render(request, 'dashboard/home.html', {'categories': categories, 'items': items})

@login_required(login_url='menu:dashboard_login')
def dashboard_item_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully!')
            return redirect('menu:dashboard_home')
    else:
        form = MenuItemForm()
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Add Menu Item'})

@login_required(login_url='menu:dashboard_login')
def dashboard_item_update(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('menu:dashboard_home')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Edit Menu Item'})

@login_required(login_url='menu:dashboard_login')
def dashboard_item_delete(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully!')
        return redirect('menu:dashboard_home')
    return render(request, 'dashboard/confirm_delete.html', {'obj': item})

@login_required(login_url='menu:dashboard_login')
def dashboard_category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('menu:dashboard_home')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Add Category'})

@login_required(login_url='menu:dashboard_login')
def dashboard_category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('menu:dashboard_home')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Edit Category'})


@login_required(login_url='menu:dashboard_login')
def dashboard_category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('menu:dashboard_home')
    return render(request, 'dashboard/confirm_delete.html', {'obj': category})
