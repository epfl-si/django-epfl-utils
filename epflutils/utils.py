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
    SLB monitors this function to know if it can use this server
    If the function returns HTTP 200, the server can be used by SLB
    """

    slb = True

    if slb:
        from django.db import connection
        cursor = connection.cursor()

        cursor.execute("show tables")
        tables = cursor.fetchall()

        status = 200

        cursor.execute("check table " + ','.join(t[0] for t in tables))
        for result in cursor.fetchall():
            if result[2].lower() == 'error':
                status = 500
                break

    else:
        status = 500

    response = render(request, "check.html", {'status': status})
    response.status_code = status
    return response
