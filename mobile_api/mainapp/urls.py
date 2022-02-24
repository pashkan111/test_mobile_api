from django.urls import path, include
from . import views


urlpatterns = [
    path('shops', views.ShopListView.as_view())
]
