# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from models import Room, Picture, Property


# Create your views here.
class HomePageView(ListView):
    template_name = 'index.html'
    model = Room
    context_object_name = 'rooms'
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)
