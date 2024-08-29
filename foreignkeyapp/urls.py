from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'), 
    path('add_course',views.add_course,name='add_course'),
    path('add_student/',views.add_student,name='add_student'),
    path('show_details/',views.show_details,name='show_details'),

    path('add_coursedb',views.add_coursedb,name="add_coursedb"),
    path('add_studentdb',views.add_studentdb,name="add_studentdb"),
    path('edit/<int:pk>',views.edit, name='edit'),
    path('editdb/<int:pk>',views.editdb,name='editdb'),
    path('delete/<int:pk>',views.delete,name='delete'),
    
    # path('logout/',views.logout,name="logout"),
    
]