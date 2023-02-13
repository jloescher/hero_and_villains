from django.urls import path
from .views import SuperView, super_detail

urlpatterns = [
    path("supers", SuperView.as_view(), name="supers"),
    path("supers/<int:pk>", super_detail, name="super-detail"),
]
