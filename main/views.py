from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406495836',
        'name': 'Z Arsy Alam Sin',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
