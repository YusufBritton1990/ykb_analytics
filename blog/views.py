from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    #From Post model, gather posts that were publisted before now and order by
    # its publisted date, descending order
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # renders html if blog is requested from urls
    return render(request, 'blog/post_list.html',{"posts":posts})
