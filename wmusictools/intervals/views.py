from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.

def intervals (request):
    docHtml = open("intervals/templates/intervalsPage.html")
    plt = Template(docHtml.read())
    docHtml.close()
    ctx = Context ()

    return HttpResponse (plt.render(ctx))

def checkinterval (request):

    return HttpResponse ("check")

def createinterval (request):

    return HttpResponse ("create")
