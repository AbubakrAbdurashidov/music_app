from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView


class EpisodeListView(TemplateView):
    template_name = 'episode/episodes_list.html'


class EpisodeDetailView(TemplateView):
    template_name = 'episode/episode_detail.html'