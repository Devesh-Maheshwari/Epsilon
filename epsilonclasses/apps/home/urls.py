from django.urls import path
from . import views



app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='aboutus'),
    path('course/',views.course,name='course'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact')

]
