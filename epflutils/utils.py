
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


models.pymodels.py

def check(request):
    """
    Cette méthode permet au SLB de vérifier si le serveur peut être utilisé.

    Si la méthode retourne HTTP 200 le noeud est utilisé par le SLB
    Si la méthode retourne HTTP 500 le noeud ne peut pas être utilisé.

    # -------------------------------------------------------------------------------------------
    # EXEMPLE DE COMMANDE CHECK
    # mysql> check table forms;
    # +--------------+-------+----------+-------------------------------------------------------+
    # | Table        | Op    | Msg_type | Msg_text                                              |
    # +--------------+-------+----------+-------------------------------------------------------+
    # | inForm.forms | check | warning  | 1 client is using or hasn't closed the table properly |
    # | inForm.forms | check | error    | Wrong bytesec: 34-104-101 at linkstart: 58025108      |
    # | inForm.forms | check | error    | Corrupt                                               |
    # +--------------+-------+----------+-------------------------------------------------------+
    # 3 rows in set (0.06 sec)
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