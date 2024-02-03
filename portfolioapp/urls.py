from django.urls import path
from .views import index,contact,work,blog,about,services

urlpatterns = [
    path('', index,),
    path('contact/', contact, name='contact.html'),
    path('work/', work, name='work.html'),
    path('blog/', blog,name='blog.html'),
    path('about/', about,name='about.html'),
    path('services/', services,name='services.html'),
]