from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm, AccountSettingsForm, UploadForm, CommentForm
from django.contrib import messages
from .models import Video, Comments


User = get_user_model()


def enter_page(request):
    return render(request, 'entrance.html')

@login_required
def home_page(request):
    return render(request, 'home.html')


@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = LoginForm()
    return render(request=request, template_name='login.html', context={'login_form': form})

def register_request(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Registration properly ended.')
            return redirect('homepage')
        else:
            messages.error(request, f'Registration failed, try again', redirect('register/'))
    form = RegistrationForm()
    return render(request=request, template_name='register.html', context={'register_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, f'You have been successfully logged out')
    return redirect('login')


@login_required
def profile(request):
    if request.method == "POST":
        form = AccountSettingsForm(request.POST, instance=request.user)
        update = form.save()
        update.user = request.user
        update.save()
    else:
        form = AccountSettingsForm()
    return render(request, 'profile.html', context={'form': form})


@login_required
def account_settings(request):
    if request.method == "POST":
        form = AccountSettingsForm(request.POST, instance=request.user)
        update = form.save()
        update.user = request.user
        update.save()
    else:
        form = AccountSettingsForm()
    return render(request, 'account-settings.html', context={'update-form': form})


@login_required
def gallery_view(request):
    return render(request, 'gallery.html')


@login_required
def videos_view(request):
    video = Video.objects.all()
    return render(request, 'videos.html', context={'video': video})


@login_required
def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES or None)
        if form.is_valid():
            if form.is_valid():
                new_video = form.save()
                new_video.author = request.user
                new_video.save()
            return redirect('/upload/')
    else:
        form = UploadForm()

    context = {
        'form': form
    }
    return render(request, 'upload.html', context)


@login_required
def video_item_view(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    comments = Comments.objects.filter(video=video)
    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user, video=video)
        if form.is_valid():
            form.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'vid.html', {'video': video, 'comments': comments, 'comment_form': form})
