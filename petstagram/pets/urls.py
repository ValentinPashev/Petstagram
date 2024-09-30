from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet_page, name='add_page'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page, name='pet-details'),
        path('edit/', views.pet_edit_page, name='edit-page'),
        path('delete/', views.pet_delete_page, name='delete-page'),
    ]))
]