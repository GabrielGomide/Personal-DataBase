from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('people/', people, name='people'),
    path('people/add/', add, name='add'),
    path('people/<int:id>', person, name='person'),
    path('people/<int:id>/edit', edit_person, name='edit_person'),
    path('notes/', notes, name='notes'),
    path('notes/add', add_note, name='add_note'),
    path('notes/<int:id>', note, name='note'),
    path('notes/<int:id>/edit', edit_note, name='edit_note'),
    path('notes/<int:id>/delete', delete_note, name='delete_note'),
    path('folders/<int:id>', folder, name='folder'),
    path('folders/edit/<int:id>', edit_folder, name='folder'),
    path('folders/<int:id>/delete', delete_folder, name='delete_folder')
]
