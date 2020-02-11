from django.conf.urls import url
from hotel_app import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url


# TEMPLATE TAGGING
app_name= 'hotel_app'
urlpatterns = [

    path('bookings/', views.bookings_list, name='bookings_list'),
    path('book_update/<int:id>', views.book_update, name='book_update'),
    path('book_add/', views.book_add, name='book_add'),
    path('book_delete/<int:id>', views.book_delete, name='book_delete'),


    path('clients/', views.client_add, name='clients'),
    path('client_update/<int:id>', views.client_update, name='client_update'),
    #path('client_add/', views.client_add, name='client_add'),
    path('client_delete/<int:id>', views.client_delete, name='client_delete'),
    path('client_display_info/<int:id>', views.client_display_info, name='client_display_info'),
        ]
