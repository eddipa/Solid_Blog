from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.db import models


class CustomUser(AbstractUser):
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

