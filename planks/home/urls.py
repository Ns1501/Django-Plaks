from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.sevices,name='services'),
    path('contact',views.contact,name='contact')
]
