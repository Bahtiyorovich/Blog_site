from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list_posts.html'


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status = 'published', publish_year=year, publish_month=month, publish_day=day)
    return render(request, 'blog/post/detail_post.html', {'post': post})