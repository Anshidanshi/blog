
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from . models import *
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ipware import get_client_ip

User = get_user_model()

def post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    comment_data = []
    for comment in comments:
        user = User.objects.get(first_name=comment.author)

        user_data = {
            
            'author': user.first_name,
          
           
            # Add other user properties as needed
        }


        comment_data.append({
            'author': user_data,
            'content': comment.comment,
            #'timestamp': comment.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            'id':comment.id,
         
            
        })

    post_data = {      
        'comments': comment_data
    }

    return JsonResponse(post_data)


def post_list(request):
    posts = Post.objects.order_by('-visitors_count')[:5]
    olderpost = Post.objects.order_by('created_at')[:6]
    flash = breakingnew.objects.get(id=1)
    highlights = highlight.objects.get(highlight='True')[:3]
    #ho = Post.objects.filter(high=highlights)
    return render(request, 'index.html', {'post':posts,'oldpost':olderpost,'flash':flash,'highlight':ho})

def post_view(request, id):
    if request.method == 'POST':        
        comment = request.POST.get('comment') 
        post = Post.objects.get(id=id)
        author = request.user
        Comment.objects.create(
            author=author,
            post=post,
            comment=comment,

        )

        return JsonResponse({'success': True})
    
    post = Post.objects.get(id=id)
    user = User.objects.get(first_name=post.author) 
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    visitor_ip = get_client_ip(request)

    # Check if the visitor has already visited this post
    visitor_exists = Visitor.objects.filter(ip_address=visitor_ip, post=post).exists()

    if not visitor_exists:
        # Create a new Visitor instance and associate it with the post
        Visitor.objects.create(ip_address=visitor_ip, post=post)
        
        post.visitors_count += 1
        post.save()

    

    return render(request, 'post.html', {'post':post,'comments':comments,'user':user})


def delete(request,id): 
    referring_url = request.META.get('HTTP_REFERER')   
    comment = Comment.objects.get(id=id)
    if request.user == comment.author:
        comment.delete()
        return redirect(referring_url)
    else:
        
        return HttpResponse('you are not allowed')


