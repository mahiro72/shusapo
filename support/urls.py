from django.contrib import admin
from django.urls import path
from . import views

app_name ="support"

urlpatterns = [
    path('top/', views.Top.as_view(), name='top'),
    path('home/',views.home,name='home'),
    path('home/contact',views.contact,name='contact'),
    path('top/comment_create',views.CommentCreate.as_view(),name='comment_create'),

]