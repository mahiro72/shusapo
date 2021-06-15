from django.shortcuts import render
from django.views import generic
from .models import Company,SAnalysis,IAnalysis,ES
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from .forms import CompanyForm,SAnalysisForm,ESForm,IAnalysisForm
from django import forms
from django.http import HttpResponse
from django.utils import timezone
# Company

class CompanyList(generic.ListView):
    # company = Company.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

    model = Company
    template_name = 'board/company_list.html'


class CompanyCreate(generic.FormView,LoginRequiredMixin):
    form_class = CompanyForm
    template_name ="board/company_create.html"
    success_url = reverse_lazy('board:company_list')
    
    def form_valid(self, form):
        # 入力フォームの形が正しい形で送信されてきたときに行われる処理
        qryset =  form.save(commit=False)
        qryset.post_user=self.request.user
        qryset.save()
        return super().form_valid(form)

class CompanyDetail(generic.DetailView):
    model = Company
    template_name = 'board/company_detail.html'


# SelfAnalysis

class SAnalysisList(generic.ListView):
    model = SAnalysis
    template_name = 'board/sanalysis_list.html'


class SAnalysisCreate(generic.FormView,LoginRequiredMixin):
    form_class = SAnalysisForm
    template_name ="board/sanalysis_create.html"
    success_url = reverse_lazy('board:sanalysis_list')
    
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.post_user=self.request.user
        qryset.save()
        return super().form_valid(form)

class SAnalysisDetail(generic.DetailView):
    model = SAnalysis
    template_name = 'board/sanalysis_detail.html'



# ES

class ESList(generic.ListView):
    model = ES
    template_name = 'board/es_list.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        es = ES.objects.all().values()
        new_es = []
        for e in es:
            if e['post_user_id'] == self.request.user.id:
                new_es.append(e)
        context['new_es'] = new_es
        return context


class ESCreate(generic.FormView,LoginRequiredMixin):
    form_class = ESForm
    template_name ="board/es_create.html"
    success_url = reverse_lazy('board:es_list')
    
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.post_user=self.request.user
        qryset.save()
        return super().form_valid(form)


# intern
import requests
from bs4 import BeautifulSoup

def search():
    site = requests.get('https://job.mynavi.jp/22/pc/search/new_corps.html?OP:1&func=PCtop')
    soup = BeautifulSoup(site.text, 'html.parser')
    a_text_href = []
    for i in range(50):
        id1 = 'corpNameLink['+str(i)+']'
        id2 = 'btnEntry['+str(i)+']'

        s = soup.find(id=id1)
        s2 = soup.find(id=id2)

        text = s.text
        href = s.get('href')
        href2 = s2.get('href')
        if s:
            a_text_href.append({'text':text[:-4],'href':href,'href2':href2})
    return a_text_href


class InternList(generic.TemplateView):
    template_name = 'board/intern_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['a_text_href']= search()
        return context






# ianalysis


class IAnalysisList(generic.ListView):
    model = IAnalysis
    template_name = 'board/ianalysis_list.html'


class IAnalysisCreate(generic.FormView,LoginRequiredMixin):
    form_class = IAnalysisForm
    template_name ="board/ianalysis_create.html"
    success_url = reverse_lazy('board:ianalysis_list')
    
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.post_user=self.request.user
        qryset.save()
        return super().form_valid(form)

class IAnalysisDetail(generic.DetailView):
    model = IAnalysis
    template_name = 'board/ianalysis_detail.html'

