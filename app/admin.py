from django.contrib import admin
from .models import WikiPage, PageVersion

admin.site.register(WikiPage)
admin.site.register(PageVersion)
