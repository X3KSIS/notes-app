from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Notes
from .forms import NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/index.html'
    context_object_name = 'notes'
    ordering = ['-created']

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:list')

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:list')

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)
