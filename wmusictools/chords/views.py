from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.

def chords (request):
    docHtml = open("chords/templates/chordsPage.html")
    plt = Template(docHtml.read())
    docHtml.close()
    ctx = Context ()

    return HttpResponse (plt.render(ctx))

def checktriad (request):
    docHtml = open("chords/templates/checktriad.html")
    plt = Template(docHtml.read())
    docHtml.close()
    ctx = Context ()

    return HttpResponse (plt.render(ctx))

def checkcuat (request):
    docHtml = open("chords/templates/checkcuat.html")
    plt = Template(docHtml.read())
    docHtml.close()
    ctx = Context ()

    return HttpResponse (plt.render(ctx))

def createtriad (request):
    docHtml = open("chords/templates/createtriad.html")
    plt = Template(docHtml.read())
    docHtml.close()
    ctx = Context ()

    return HttpResponse (plt.render(ctx))
    
def createcuat (request):
    docHtml = open("chords/templates/createcuat.html")
    plt = Template(docHtml.read())
    docHtml.close()
    ctx = Context ()

    return HttpResponse (plt.render(ctx))

def dochecktriad (request):
#    rootNote = str (request.POST['root'])
#    thirdNote = str (request.POST['third'])
#    fiftNote = str (request.POST['fift'])

    return HttpResponse("Datos cargados")

def docheckcuat (request):
#    rootNote = str (request.POST['root'])
#    thirdNote = str (request.POST['third'])
#    fiftNote = str (request.POST['fift'])
#    sevenNote = str (request.POST['seven'])

    return HttpResponse("Datos cargados")

def docreatetriad (request):
#    rootNote = str (request.POST['root'])
#    tipeTriad = str (reques.POST['ttype'])

#Problemas con el boton de enviar

    return HttpResponse("Datos cargados")

def docreatecuat (request):
#    rootNote = str (request.POST['root'])
#    tipeCuat = str (reques.POST['ctype'])

#Problemas con el boton de enviar
    
    return HttpResponse("Datos cargados")
