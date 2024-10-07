import datetime
from django.shortcuts import render, redirect
from main.form import AtributEntryForm
from main.models import AtributEntery
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm' : '2306165566',
        'name': request.user.username,
        'class': 'PBP C',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def add_atribute_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    image_url = request.POST.get("image_url")
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    quantity = request.POST.get("quantity")
    user = request.user

    new_product = AtributEntery(
        name = name, image_url = image_url,
        price = price, description = description,
        quantity = quantity, 
        user = user
    )
    new_product.save()
    return HttpResponse(b"CREATED", status=201)
    

def create_atribute_entry(request):
    form = AtributEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        atribute_entry = form.save(commit=False)
        atribute_entry.user =request.user
        atribute_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_atribute_entry.html", context)

def show_xml(request):
    data = AtributEntery.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = AtributEntery.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = AtributEntery.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = AtributEntery.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
          messages.error(request, 'Invalid username or password.')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = AtributEntery.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = AtributEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    product = AtributEntery.objects.get(pk = id)
    # Hapus mood
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def halaman_depan(request):
    return render(request, 'halaman_depan.html')