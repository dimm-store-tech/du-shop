from django.urls import path
from .import views
urlpatterns = [
    path('',views.index , name='index'),
    path('producto/<int:id>', views.producto, name='producto')
]
