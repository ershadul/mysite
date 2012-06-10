# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from posts.models import Post
from comments.forms import CommentForm

def index(request):
    post_list = Post.objects.all()
    
    return render_to_response('posts/index.html', { 'post_list': post_list })
    
def details(request, post_id):
    message = ''
    try:
        post = Post.objects.get(pk=post_id)
        
        if request.method == 'POST':
            data = request.POST.copy()
            form = CommentForm(data)
            if form.is_valid():
                # save
                form.save()
                return HttpResponseRedirect('/posts/index')
            else:
                errors = form.errors
        else:
            form = CommentForm()
            data = {}
                
    except Post.DoesNotExist, e:
        message = str(e)
        post = None
    
    context = RequestContext(request)
    context.update({ 'post': post, 'message': message,
        'form': form, 'data': data })
    return render_to_response('posts/details.html', context)
    
def test(request, post_id, post_title):
    return HttpResponse('Testing...')
    
