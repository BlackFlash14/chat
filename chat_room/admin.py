from django.contrib import admin
from .models import Room
# from django.contrib.auth.models import User

class RoomAdmin(admin.ModelAdmin):
    # filter_horizontal = ('invited',)
    list_display = ("creator", "date", "invited_users")
    def invited_users(self, obj):
        return "\n".join([p.username for p in obj.invited.all()])

# Register your models here.
admin.site.register(Room, RoomAdmin)
