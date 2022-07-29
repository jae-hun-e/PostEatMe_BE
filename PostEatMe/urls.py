from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
# from users.views import UserViewSet
from users import views as user
from memo import views as memo

# router = routers.DefaultRouter()
# router.register('users', UserViewSet)

urlpatterns = [
    path('user/', user.UserListCreate.as_view()),
    path('user/delete_all', user.del_user),
    path('memo/', memo.MemoListCreate.as_view()),
    path('memo/<str:name>', memo.del_data),
    # path('memo/<str:phone>', memo.MemoListCreate.as_view())
    # path('', include(router.urls)),

]
