from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('company/',views.CompanyList.as_view(),name='company_list'),
    path('company/create/',views.CompanyCreate.as_view(),name='company_create'),
    path('company/detail/<int:pk>',views.CompanyDetail.as_view(),name='company_detail'),

    path('sanalysis/',views.SAnalysisList.as_view(),name='sanalysis_list'),
    path('sanalysis/create/',views.SAnalysisCreate.as_view(),name='sanalysis_create'),
    path('sanalysis/detail/<int:pk>',views.SAnalysisDetail.as_view(),name='sanalysis_detail'),

    path('ianalysis/',views.IAnalysisList.as_view(),name='ianalysis_list'),
    path('ianalysis/create/',views.IAnalysisCreate.as_view(),name='ianalysis_create'),
    path('ianalysis/detail/<int:pk>',views.IAnalysisDetail.as_view(),name='ianalysis_detail'),


    path('es/',views.ESList.as_view(),name='es_list'),
    path('es/create/',views.ESCreate.as_view(),name='es_create'),

    path('intern/',views.InternList.as_view(),name='intern_list'),
]