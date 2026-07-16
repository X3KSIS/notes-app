from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Title',
        help_text='Note Title'
    )
    description = models.TextField(
        null=False,
        blank=False,
        help_text='Write your note',
        verbose_name='Description'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created']
