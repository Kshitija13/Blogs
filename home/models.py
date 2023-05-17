from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

def user_directory_path(instance, filename):
    return 'posts/%Y/%m/%d/'.format(instance.id, filename)

class Post (models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    image= models.ImageField(upload_to="shop/images",default="")
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_posts')
    content = RichTextUploadingField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    def get_absolute_url(self):
        return reverse('post_single',args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    

    
