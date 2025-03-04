from . import views
from django.urls import path

urlpatterns = [
    path('',views.emp_list,name='list'),
    path('create/',views.create,name='create'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),

]