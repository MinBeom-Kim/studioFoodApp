from django.urls import path
from . import views

app_name = "apps"

urlpatterns = [
    path("", views.ClassListView, name="list"),
    # path("detail/<int:pk>/", views.ClassDetail.as_view(), name="detail"), 
    path('detail/<int:class_id>/', views.class_detail, name='class_detail'),
]
