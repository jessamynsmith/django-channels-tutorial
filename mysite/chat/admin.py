from django.contrib import admin
from chat import models as chat_models


@admin.register(chat_models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(chat_models.RoomUser)
class RoomUserAdmin(admin.ModelAdmin):
    pass
