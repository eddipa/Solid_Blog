from django.contrib.auth.models import AbstractUser, Group
from django.template.defaultfilters import slugify
from django.db import models


# TODO: post save signal to set user as staff when a group is assigned
def make_user_staff(self):
    groups = self.groups.all()
    manager_group = Group.objects.filter(name='Manager').first()
    writer_group = Group.objects.filter(name='Writer').first()
    if manager_group in groups or writer_group in groups:
        self.is_staff = True


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


