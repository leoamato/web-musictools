from django.http import HttpResponse
from django.template import Template, Context

def principalPage (request):
    docHtml = open("wmusictools/templates/principalPage.html")
    plt = Template(docHtml.read())
    docHtml.close()
    ctx = Context ()

    return HttpResponse (plt.render(ctx))