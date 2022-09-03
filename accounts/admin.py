from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

from posts.models import Post


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['username', 'is_superuser', 'is_active', 'is_staff', "staff_group", 'posts']

    ordering = ['is_superuser', 'is_active', 'is_staff']

    def staff_group(self, obj):
        group = Group.objects.filter(user=obj)
        return [g for g in group]

    def posts(self, obj):
        posts = Post.objects.filter(author=obj).count()
        return posts

    def __init__(self, *args, **kwargs):

        # manager group
        manager_group = Group.objects.filter(name='Manager')
        if manager_group.count() == 0:
            # TODO: add permissions
            print('no manager group')

        # writer group
        writer_group = Group.objects.filter(name='Writer')
        if writer_group.count() == 0:
            # TODO: add permissions
            print('no writer group')

        super(CustomUserAdmin, self).__init__(*args, **kwargs)


admin.site.register(CustomUser, CustomUserAdmin)
