from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import DetailView

from chat import models as chat_models


def index(request):
    return render(request, 'chat/index.html')


class RoomView(LoginRequiredMixin, DetailView):
    template_name = 'chat/room.html'
    model = chat_models.Room
    slug_field = 'name'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        room_user = self.object.roomuser_set.filter(user=self.request.user).first()
        if not room_user:
            return HttpResponseForbidden()
        return response
