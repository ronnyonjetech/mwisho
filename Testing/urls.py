from  . import views

from django.urls import path

urlpatterns = [
    path("results",views.testtest,name="testing"),
    path('add',views.add,name='add')
     
]