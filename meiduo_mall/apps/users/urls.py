from django.urls import path

from apps.users import views

urlpatterns = [
    path('usernames/<username:username>/count/', views.RegisterName.as_view()),
    path('mobiles/<mobile:mobile>/count/', views.RegisterMobile.as_view()),
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('info/', views.UserInfo.as_view()),
]
