from django.shortcuts import render
from django.views import generic
from . import models
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
# Create your views here.

class Top(generic.TemplateView):
    template_name = 'support/top.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        comments = models.Comment.objects.all()
        context['comments'] = comments
        return context


def home(request):
    return render(request, 'support/home.html') 


def contact(request):
    return render(request, 'support/contact.html') 


class CommentCreate(generic.FormView,LoginRequiredMixin):
    form_class = forms.CommentForm
    template_name ="support/comment_create.html"
    success_url = reverse_lazy('support:top')
    
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.post_user=self.request.user
        qryset.save()
        return super().form_valid(form)
