from django.urls import path
from .views import (
    SuperView,
    SuperDetailView,
    SuperDeleteView,
    SuperUpdateView,
)

urlpatterns = [
    path("supers", SuperView.as_view(), name="super-list"),
    path("supers/<int:pk>", SuperDetailView.as_view(), name="super-detail"),
    path("supers/<int:pk>", SuperUpdateView.as_view(), name="super-update"),
    path("supers", SuperView.as_view(), name="super-create"),
    path("supers/<int:pk>", SuperDeleteView.as_view(), name="super-delete"),
]
