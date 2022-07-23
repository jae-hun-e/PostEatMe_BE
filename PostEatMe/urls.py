from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from users import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('user/start_app', views.test_html),
    path('user'
         '/map_main', views.UserListCreate.as_view()),
    path('', include(router.urls)),

]
