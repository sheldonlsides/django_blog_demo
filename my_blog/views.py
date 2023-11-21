from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    post_list = Post.published.all()

    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # sets current page to first page
        posts = paginator.page(1)
    except EmptyPage:
        # sets current page to last page
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html',
                  {'posts' : posts})

# def post_detail(request, id):
def post_detail(request, year, month, day, post):
    # alternate way of writing the same method
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found")
    
    # return  render(request, 'blog/post/detail.html',
    #                {'post': post})
  
    # retrieving post with the id
    # post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED, 
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
   
    return  render(request, 'blog/post/detail.html',
                   {'post': post})