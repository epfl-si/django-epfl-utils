import django.utils.translation
from django.shortcuts import redirect, render


def switch_language_and_redirect(request, url, lang):
    """
    User can choose the interface language
    """
    if request.LANGUAGE_CODE != lang:
        django.utils.translation.activate(lang)
        request.session['django_language'] = lang
    return redirect('/' + '?'.join([url, request.GET.urlencode()]))


def check(request):
    """
    Cette méthode permet au SLB de vérifier si le serveur peut être utilisé.

    Si la méthode retourne HTTP 200 le noeud est utilisé par le SLB
    Si la méthode retourne HTTP 500 le noeud ne peut pas être utilisé.
    """

    slb = True

    if slb:

        from django.db import connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("show tables")
            status = 200
        except:
            status = 500

    else:
        status = 500

    response = render(request, "check.html", {'status': status})
    response.status_code = status
    return response
