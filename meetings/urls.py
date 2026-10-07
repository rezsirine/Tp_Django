from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.get_all_view, name='getall'),
    path('detail/<int:id>/', views.detail_view, name='detail'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
    path('create/', views.create_view, name='create'),
    path('update/<int:id>/', views.update_view, name='update'),
]