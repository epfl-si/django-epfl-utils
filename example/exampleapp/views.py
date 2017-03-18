from django.shortcuts import render


def homepage(request):

    return render(request, 'exampleapp/index.html', {
        'foo': 'bar',
    })

