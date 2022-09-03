from django.contrib import admin

from .models import Post, Category, Tag

# TODO: delete counter from admin menu
admin.site.register([Post, Category, Tag])
