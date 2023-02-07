from django.contrib import admin
from file_resubmit.admin import AdminResubmitMixin

from polls.models import Polls


class PollsAdmin(AdminResubmitMixin, admin.ModelAdmin):
    pass


admin.site.register(Polls, PollsAdmin)
