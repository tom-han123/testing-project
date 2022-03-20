from django.urls import path
from . import views

app_name='tests'
urlpatterns =[
        path('',views.landing,name='landing'),
        path('home/',views.home,name='home'),
        path('test/<int:pk>/',views.index,name='index'),
        path('<int:pk>/results/',views.results,name='results'),
]