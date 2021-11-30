from django.conf import settings
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)

    def get_user_names(self):
        users = self.roomuser_set.order_by('user__username')
        usernames = users.values_list('user__username', flat=True)
        return usernames

    def __str__(self):
        user_names = ','.join(self.get_user_names())
        return f'{self.name} - {user_names}'


class RoomUser(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room.name} - {self.user.username}'
