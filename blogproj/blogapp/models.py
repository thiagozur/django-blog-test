from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    class NewManagerD(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='draft')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogapp_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    excerpt = models.TextField(null=True)
    objects = models.Manager()
    newmanager = NewManager()
    newmanagerd = NewManagerD()

    def septext(self):
        if '\n' in self.content:
            return self.content.split('\n')
        else:
            return [self.content]

    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class PostCounter(models.Model):
    countid = models.BigAutoField(primary_key=True)
    slug = models.SlugField(max_length=250, null=True)
    
    class Meta:
        verbose_name = 'Post Counter'
        verbose_name_plural = 'Post Counter'

    def __str__(self):
        return f'Post {self.countid}'