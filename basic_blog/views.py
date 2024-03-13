from django.shortcuts import render, redirect
from .models import Post, Tag
from django.contrib.auth.decorators import login_required


def post_list(request):
    
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    
    posts = Post.objects.get(pk=pk)
    context = {
        'posts' : posts,
        'pk' : pk,
    }
    return render(request, "blog/post_detail.html", context)

@login_required
def post_write(request):

    if request.method == 'POST':
        post = Post.objects.create(
            user=request.user,
            title=request.POST['title'],
            contents=request.POST['contents'],
            img=request.POST['img'],
        )
        tag_names = request.POST['tags'].split(', ') 
        
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name.strip())
            post.tags.add(tag)
        return redirect('/blog')

    return render(request, 'blog/post_write.html')

@login_required
def post_delete(request, pk):

    post = Post.objects.get(pk=pk)

    if post.user != request.user:
        return redirect('/blog')  # 사용자를 보내고 싶은 페이지로 리다이렉트

    if request.method == 'POST':
        post.delete()
        return redirect('/blog')
    return render(request, 'blog/post_delete.html', {'Post': post})

@login_required
def post_edit(request, pk) :

    post = Post.objects.get(pk=pk)

    if post.user != request.user:
        return redirect('/blog')  # 사용자를 보내고 싶은 페이지로 리다이렉트
    
    if request.method == 'POST' :
        post.title = request.POST.get('title')
        post.contents = request.POST.get('contents')
        post.save()
        return redirect('/blog', pk=post.pk)
    else :
        context = {'post' : post}
        return render(request, 'blog/post_edit.html', context)

def post_search(request, tags):

    posts = Post.objects.filter(tags__name__icontains=tags).order_by('-created_at')
    return render(request, 'blog/post_search.html', {'posts': posts, 'tags': tags})