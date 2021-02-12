from django.contrib import admin
from .models import Consultant, UserProfile, Blog, Event

admin.site.register(Consultant)
admin.site.register(UserProfile)
admin.site.register(Blog)
admin.site.register(Event)
# Register your models here.
