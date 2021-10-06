
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('index2',views.index2,name='index2'),
    path('menu',views.menu,name='menu'),
    path('faq',views.faq,name='faq'),
    path('team',views.team,name='team'),
    path('gallery',views.gallery,name='gallery'),
    path('restaurant',views.restaurant,name='restaurant'),
    path('restaurant-details',views.restaurant_details,name='restaurant-details'),
    path('blog-standard',views.blog_standard,name='blog-standard'),
    path('blog-details',views.blog_details,name='blog-details'),
    path('contact',views.contact,name='contact'),
]
