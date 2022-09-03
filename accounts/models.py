from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.db import models

from django.contrib import admin


from django.utils.html import format_html


class CustomUser(AbstractUser):
    slug = models.SlugField(null=False, unique=True)

    # TODO: change color for specific user type like premium
    '''
    @admin.display
    def user(self):
        if self.is_superuser:
            return format_html(
                '<span style="color: Green;">{}</span>',
                self.username,
            )
        return self.username
    '''

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

