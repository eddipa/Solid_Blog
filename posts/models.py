from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from accounts.models import CustomUser as Author


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    class STATES(models.TextChoices):
        DRAFT = 'draft'
        PUBLISHED = 'published'
        ARCHIVED = 'archived'

    title = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    state = models.CharField(max_length=10, choices=STATES.choices, default=STATES.DRAFT)
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    image = models.FileField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        # slug
        if not self.slug:
            self.slug = slugify(self.title)
        # user
        # image
        if self.image:
            this = Post.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
