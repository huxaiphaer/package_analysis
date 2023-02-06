from django.contrib import admin
from django_reverse_admin import ReverseModelAdmin

from polls.models import Polls


class PollsAdmin(ReverseModelAdmin):
    """PollsAdmin"""
    inline_type = 'tabular'
    inline_reverse = ['name']


admin.site.register(Polls, PollsAdmin)

