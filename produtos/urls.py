from django.urls import path
from produtos import views

urlpatterns =[
    path('', views.index),
    path('add/', views.new_produto, name='addprod')
]
