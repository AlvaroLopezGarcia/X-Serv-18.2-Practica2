from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Url

FORMULARIO = """
    <form action= "/" Method= "POST">
    URL:<br>
    <input type="text" name="URL" ><br>
    <input type="submit" value="Enviar">
</form>
"""

def checkUrl(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "http://" + url

def buscaUrl(url):
    found= False
    if url != '':
        url = checkUrl(url)
        lista = Url.objects.all()
        for web in lista:
            web = str(web)
            if web == url:
                found= True
                break
        if found != True or len(lista) == 0:
            url = Url(dir = url)
            url.save()

@csrf_exempt
def barra(request):
    
    if request.method == "POST":
        url = Url(dir = request.POST['URL'])
        url = str(url)
        buscaUrl(url)    
    lista = Url.objects.all()
    respuesta = "<ul>"
    for url in lista:
        respuesta += '<li><a href="' + url.dir + '">' + str(url.id) + ", " + url.dir + "</a><br/>"
    respuesta += "</ul>"
    respuesta = "<html><body><h1>" + FORMULARIO + "</h1><p>"+ respuesta +"</p></body></html>"
    return HttpResponse (respuesta)
 
