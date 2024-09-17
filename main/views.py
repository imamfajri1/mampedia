from django.shortcuts import render, redirect
from main.form import AtributEntryForm
from main.models import AtributEntery
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    atribut_entries = AtributEntery.objects.all()
    context = {
        'npm' : '2306165566',
        'name': 'Imam Fajri',
        'class': 'PBP C',
        'atribut_entries': atribut_entries,
    }

    return render(request, "main.html", context)

def create_atribute_entry(request):
    form = AtributEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_atribute_entry.html", context)

def show_xml(request):
    data = AtributEntery.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = AtributEntery.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = AtributEntery.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = AtributEntery.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")