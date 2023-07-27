from django.contrib import admin

# Register your models here.
from .models import User, Event, Expense, Attendee, Task
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Expense)
admin.site.register(Attendee)
admin.site.register(Task)
