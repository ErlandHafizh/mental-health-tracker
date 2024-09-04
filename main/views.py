from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165686',
        'name': 'Erland Hafizh Aristovi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)