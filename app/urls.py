from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_new_record, name='add'),
    path('page/<int:record_id>/', views.view_record, name='page'),
    path('edit/<int:record_id>/', views.edit_record, name='edit'),
    path('delete/<int:record_id>/', views.delete_record, name='delete')
]
