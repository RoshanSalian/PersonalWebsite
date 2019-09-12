from django.urls import path
from . import views
# post list is the first page
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
