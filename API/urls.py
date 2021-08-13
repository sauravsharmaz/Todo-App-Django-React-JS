from django.urls import path
from API import views

urlpatterns = [
    path('create',views.create),
    path('retrieve',views.retrieve),
    path('retrieve/<int:ID>',views.retrieveByid),
    path('update/<int:ID>',views.update),
    path('delete/<int:ID>',views.delete),
]
