from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Sate Pacil',
        'price': 'Rp.15.000',
        'quantity': '1',
        'description': 'Sate adalah makanan ayam yang sangat enak',
    }

    return render(request, "main.html", context)