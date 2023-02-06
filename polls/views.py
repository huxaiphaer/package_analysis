"""Views.py files"""
from rest_framework import viewsets
from rest_framework.response import Response

from polls.models import Polls


class PollsDetailsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Response(list(Polls.objects.filter(id=self.kwargs['id'])))


class PollsViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        return Response(list(Polls.objects.all().values('name')))
