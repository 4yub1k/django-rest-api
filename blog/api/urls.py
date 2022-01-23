from django.urls import path, include
from . import views
from rest_framework.authtoken import views as token_view

urlpatterns = [
    #if you have created class in views then
    #path('',views.list_post.as_view(), name='list_post')
    path('',views.list_post, name='list_post'),
    path('<int:post>/',views.detail_post, name='detail_post'),
    path('register/',views.registeruser, name='reg_user'),
    path('login/',token_view.obtain_auth_token, name="api-token-auth"), #built in login
    #path('',views.index, name='index')
]

#login pass value
# {
#     "username":"username of user"
#     "password":"password of user"
# }

#login return
# {
#     "token": "6a170a175f0c936c3b94c2e8f662e0148d1ac6ef"
# }