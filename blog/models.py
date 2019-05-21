from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """
    author: Connection to User app. establish relationship to User
        on_delete: if user is deleted, comments are deleted
    title = title of post
    text = text of post
    created_date = date post is created
    published_date = updated time of post, if edited
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # If post is edited, will update time
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # This will return the title 
        return self.title
