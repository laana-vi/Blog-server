from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostOjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts', default='https://res.cloudinary.com/dpj7zvqzs/image/upload/v1614562523/media/posts/default_dhjiv8.png')
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='timestamp')
    timestamp = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts")
   

    objects = models.Manager()
    postobjects = PostOjects()

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.title
