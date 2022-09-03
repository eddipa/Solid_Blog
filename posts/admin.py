from django.contrib import admin

from .models import Post, Category, Tag

from .forms import PostForm

admin.site.site_header = 'Blog Control Panel'


# TODO: use link in author name instead of simple text
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm

    list_display = ('title', 'author', 'created_at', 'updated_at', 'state')

    list_filter = ('state', 'author',)

    # TODO: implement a search system
    # search_fields = ("author__startswith",)

    class Meta:
        ordering = ('updated_at', 'created_at')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


# TODO: delete counter from admin menu
admin.site.register([Category, Tag])
