from django.contrib import admin
from .models import Child
from .models import Schedule

admin.site.register(Schedule)
admin.site.register(Child)
