from django.contrib import admin
from .models import Room, Message,Document,Video,Links,Notify
# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Document)
admin.site.register(Video)
admin.site.register(Links)
admin.site.register(Notify)
