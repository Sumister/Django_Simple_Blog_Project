from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BLogComment
from django.contrib import messages
from blog.templatetags import extras


# For Blog Home Page
def blog_home(request):
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'blog/blogHome.html', context)


# For blog Post Page
def blog_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()

    comments = BLogComment.objects.filter(post=post, parent=None)
    replies = BLogComment.objects.filter(post=post).exclude(parent=None)
    reply_dict = {}
    for reply in replies:
        if reply.parent.sno not in reply_dict.keys():
            reply_dict[reply.parent.sno] = [reply]
        else:
            reply_dict[reply.parent.sno].append(reply)

    context = {'post': post, 'comments': comments, 'user': request.user, 'reply_dict': reply_dict}
    return render(request, 'blog/blogPost.html', context)


# For Comment and Reply
def post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        post_sno = request.POST.get('post_sno')
        post = Post.objects.get(sno=post_sno)
        parent_sno = request.POST.get('parent_sno')
        if parent_sno == "":
            comment = BLogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your Comment has been posted Successfully")
        else:
            parent = BLogComment.objects.get(sno=parent_sno)
            comment = BLogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your Reply has been posted Successfully")

    return redirect(f"/blog/{post.slug}")
