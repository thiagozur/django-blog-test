from django.utils import timezone
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, PostCounter
from .forms import NewPostForm, AuthForm, NewUserForm
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth import logout as dlogout, authenticate, login as dlogin
from django.contrib.auth.decorators import login_required

@login_required(login_url='/blog/auth/')
def home(request):
    all_posts = Post.newmanager.all()
    return render(request, 'index.html', {'posts' : all_posts})

@login_required(login_url='/blog/auth/')
def post_single(request, post):
    postsel = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post' : postsel})

@login_required(login_url='/blog/auth/')
def posting(request):
    if request.method == 'POST':
        form1 = NewPostForm(request.POST)
        if form1.is_valid():
            curpostid = PostCounter.objects.create()
            cdat = form1.cleaned_data
            curpost = Post()
            curpost.title = cdat['post_title']
            curpost.author = request.user
            curpost.slug = slugify(cdat['post_title'].lower()) + str(curpostid.countid)
            curpostid.slug = curpost.slug
            curpost.content = cdat['post_body']
            curpost.status = cdat['post_action']
            if len(cdat['post_body']) > 45:
                curpost.excerpt = cdat['post_body'][:45] + '...'
            else:
                curpost.excerpt = cdat['post_body']
            curpostid.save()
            curpost.save()  
            return HttpResponseRedirect('/blog/')
    else:
        form1 = NewPostForm()
    return render(request, 'posting.html', {'form1' : form1})

@login_required(login_url='/blog/auth/')
def postedit(request, postslug):
    if request.method == 'POST':
        editform = NewPostForm(request.POST)
        if editform.is_valid():
            edited = Post.objects.get(slug=postslug)
            cdat = editform.cleaned_data
            edited.title = cdat['post_title']
            edited.content = cdat['post_body']
            edited.status = cdat['post_action']
            edited.publish = timezone.now()
            if len(cdat['post_body']) > 45:
                edited.excerpt = cdat['post_body'][:45] + '...'
            else:
                edited.excerpt = cdat['post_body']
            edited.save()
            return HttpResponseRedirect('/blog/profile')
    else:
        edited = Post.objects.get(slug=postslug)
        post_title = edited.title
        post_body = edited.content
        post_action = edited.status
        editform = NewPostForm({'post_title' : post_title, 'post_body' : post_body, 'post_action' : post_action})
    return render(request, 'posting.html', {'form1' : editform})

@login_required(login_url='/blog/auth/')
def profile(request):
    userobj = get_object_or_404(User, username=request.user)
    pposts = Post.newmanager.all().filter(author=request.user)
    dposts = Post.newmanagerd.all().filter(author=request.user)
    return render(request, 'profile.html', {'username' : userobj.username, 'user_firstname' : userobj.first_name, 'user_lastname' : userobj.last_name, 'user_email' : userobj.email, 'pposts' : pposts, 'dposts' : dposts})

def auth(request):
    if request.method == 'POST':
        authform = AuthForm(request.POST)
        if authform.is_valid():
            authreq = authenticate(username=request.POST['username'], password=request.POST['password'])
            if authreq is not None:
                dlogin(request, authreq)
                url = request.GET.get('next')
                return HttpResponseRedirect(url)
            else:
                authform = AuthForm()
                authform.fields['username'].widget.attrs['placeholder'] = 'Usuario o contraseña incorrectos, vuelva a intentarlo'
                authform.fields['password'].widget.attrs['placeholder'] = 'Usuario o contraseña incorrectos, vuelva a intentarlo'
                return render(request, 'auth.html', {'authform' : authform})       
    else:
        authform = AuthForm()
    return render(request, 'auth.html', {'authform' : authform})

def newuser(request):
    if request.method == 'POST':
        newuserform = NewUserForm(request.POST)
        if newuserform.is_valid():
            nudata = newuserform.cleaned_data
            nuser = User.objects.create_user(username=nudata['username'], password=nudata['password'], email=nudata['email'], first_name=nudata['firstname'], last_name=nudata['lastname'])
            dlogin(request, nuser)
            return HttpResponseRedirect('/blog/')
    else:
        newuserform = NewUserForm()
    return render(request, 'newuser.html', {'newuserform' : newuserform})

@login_required(login_url='/blog/auth/')
def logout(request):
    dlogout(request)
    return render(request, 'logout.html')

@login_required(login_url='/blog/auth/')
def delpost(request, postslug):
    deleted = Post.objects.get(slug=postslug)
    deletedid = PostCounter.objects.get(slug=deleted.slug)
    deletedid.delete()
    deleted.delete()
    userobj = get_object_or_404(User, username=request.user)
    pposts = Post.newmanager.all().filter(author=request.user)
    dposts = Post.newmanagerd.all().filter(author=request.user)
    return render(request, 'profile.html', {'username' : userobj.username, 'user_firstname' : userobj.first_name, 'user_lastname' : userobj.last_name, 'user_email' : userobj.email, 'pposts' : pposts, 'dposts' : dposts})

@login_required(login_url='/blog/auth/')
def togglepost(request, postslug):
    toggled = Post.objects.get(slug=postslug)
    toggled.status = 'draft'
    toggled.save()
    userobj = get_object_or_404(User, username=request.user)
    pposts = Post.newmanager.all().filter(author=request.user)
    dposts = Post.newmanagerd.all().filter(author=request.user)
    return render(request, 'profile.html', {'username' : userobj.username, 'user_firstname' : userobj.first_name, 'user_lastname' : userobj.last_name, 'user_email' : userobj.email, 'pposts' : pposts, 'dposts' : dposts})

@login_required(login_url='/blog/auth/')
def repub(request, postslug):
    toggled = Post.objects.get(slug=postslug)
    toggled.status = 'published'
    toggled.save()
    userobj = get_object_or_404(User, username=request.user)
    pposts = Post.newmanager.all().filter(author=request.user)
    dposts = Post.newmanagerd.all().filter(author=request.user)
    return render(request, 'profile.html', {'username' : userobj.username, 'user_firstname' : userobj.first_name, 'user_lastname' : userobj.last_name, 'user_email' : userobj.email, 'pposts' : pposts, 'dposts' : dposts})

@login_required(login_url='/blog/auth/')
def redir(request):
    return HttpResponseRedirect('/blog/')