from django.urls import path

from new_app import views

urlpatterns = [
    path("",views.todo1,name="todo"),
    path("index",views.index,name="index"),
    path("index1",views.index1,name="index1"),
    path("add",views.add,name="view"),
    path("getdata",views.getdata,name="getdata"),
    path('update/<int:Todo_id>/',views.update,name='update'),
    path('delete/<int:Todo_id>/',views.delete,name='delete'),


]

