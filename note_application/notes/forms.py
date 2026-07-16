from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border focus:outline-none focus:border-indigo-500',
                'placeholder': 'Note Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border focus:outline-none focus:border-indigo-500 h-40',
                'placeholder': 'Write your note here...'
            }),
        }