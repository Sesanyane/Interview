from django.urls import path

from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('my_appointment/', views.student, name='student'),
    path('quick_appointmnet/', views.quick_appointmnet, name='quick_appointmnet'),   
    path('update/<int:id>/', views.appointment_book,name='appointment_update'),
      
]
