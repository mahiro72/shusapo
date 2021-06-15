from django.urls import path
from . import views

app_name ='accounts'

urlpatterns =[
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('registration/', views.Registration.as_view(), name='registration'),  # 追加
    path('registration/complete', views.RegistrationComp.as_view(), name='registration_complete'),  # 追加
    
]