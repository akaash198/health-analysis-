from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('predict/',views.predict,name='predict'),
    path('predict/result/',views.result),
    path('contact/',views.contact,name='contact'),
    path('about/', views.about, name='about')
    

     

]