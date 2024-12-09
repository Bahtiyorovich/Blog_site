from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import CommentForm
from .models import Post
# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list_posts.html'


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
                             slug=slug,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'blog/post/detail_post.html',
                  {'post': post,
                    'comments': comments,
                    'new_comment': new_comment,
                    'comment_form': comment_form,
                   })






