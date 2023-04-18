from django.urls import path
from cinemaapp import views

urlpatterns = [
    
    path('base',views.reuse),
    path('dashboard',views.dashboard),
    path('abc',views.abc),
    path('about',views.about),
    path('',views.index),
    path('buy',views.buy_tickets),
    path('booked',views.booked),
    path('delete/<rid>',views.delete),
    path('search',views.search),
    path('home',views.home),

]