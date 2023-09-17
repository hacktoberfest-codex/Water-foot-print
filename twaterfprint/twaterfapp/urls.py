from django.urls import path

from . import views

urlpatterns=[
    path('',views.index, name='index'),

    path('page1',views.page1, name='page1'),
    path('resultpage',views.resultpage, name='resultpage'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('divconnect1',views.divconnect1, name='divconnect1'),
    path('divconnect2',views.divconnect2, name='divconnect2'),
    path('divconnect3',views.divconnect3, name='divconnect3'),


   
   





]