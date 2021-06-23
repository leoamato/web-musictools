from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chords),
    path('checktriad/', views.checktriad),
    path('checkcuat/', views.checkcuat),
    path('createtriad/', views.createtriad),
    path('createcuat/', views.createcuat),
    path('checktriad/dochecktriad/', views.dochecktriad),
    path('checkcuat/docheckcuat/', views.docheckcuat),
    path('createtriad/docreatetriad/', views.docreatetriad),
    path('createcuat/docreatecuat/', views.docreatecuat)
]