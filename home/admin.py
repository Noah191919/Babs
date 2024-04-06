from django.contrib import admin
from .models import Testimonies
from .models import AboutMe
from .models import Blog

admin.site.register(Testimonies)
admin.site.register(AboutMe)
admin.site.register(Blog)