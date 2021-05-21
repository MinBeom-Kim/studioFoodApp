from django.urls import path
from . import views

app_name = "groups"

urlpatterns = [
    # path("", views.GroupListView.as_view(), name="list"),
    path('', views.GroupListView, name='list'),
    
    path("detail/<int:pk>", views.GroupDetail.as_view(), name="detail"),  
]