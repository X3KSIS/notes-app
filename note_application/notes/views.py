from django.shortcuts import render
from notes.models import Notes

def index(request):
    return render(request, 'notes/index.html')
