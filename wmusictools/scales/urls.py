from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.intervals),
    path('checkinterval/', views.checkinterval),
    path('createinterval/', views.createinterval)
#    path('createtriad/', views.createtriad),
#    path('createcuat/', views.createcuat),
#    path('checktriad/dochecktriad/', views.dochecktriad),
#    path('checkcuat/docheckcuat/', views.docheckcuat),
#    path('createtriad/docreatetriad/', views.docreAcordesatetriad),
#    path('createcuat/docreatecuat/', views.docreatecuat)
]