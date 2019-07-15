from django.urls import path
from .import views

urlpatterns =[
    path('',views.index, name='index'),
    path('<int:question_id>', views.changer , name='change'),
    path('number',views.number,name='number'),
]