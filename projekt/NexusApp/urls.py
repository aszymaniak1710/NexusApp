from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.display_characters, name='display_characters'),
    path('characters/<int:id_p>/', views.character_details, name='character_details'),
    path('characters/<int:id_p>/modify/', views.modify_character, name='modify_character'),
    path('characters/<int:id_p>/delete/', views.delete_character, name='delete_character'),
    path('characters/add/', views.add_character, name='add_character'),
    path('maps/', views.display_maps, name='display_maps'),
    path('ranks/', views.display_ranks, name='display_ranks'),
    path('roles/', views.display_roles, name='display_roles'),
    path('roles/<int:id_r>/delete/', views.delete_role, name='delete_role'),
    path('roles/add/', views.add_role, name='add_role'),
]

