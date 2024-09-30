from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.photo_add_page, name='add'),
    path('<int:pk>/', include([
        path('', views.photo_detail_page, name='photo-detail'),
        path('edit/', views.photo_edit_page, name='photo-edit'),
    ]))
]