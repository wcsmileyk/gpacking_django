from django.urls import path
from rest_framework.authtoken import views as drf_views
from . import views

urlpatterns = [
    path('items', views.item_list),
    path('categories', views.categories),
    path('profiles', views.profiles),
    path('packing_lists', views.packing_lists),
    path('items/<int:pk>', views.item_details),
    path('categories/<int:pk>', views.category_details),
    path('profiles/<int:pk>', views.profile_details),
    path('packing_lists/<int:pk>', views.packing_list_details),
]
