from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView, View, CreateView, UpdateView,DeleteView

from account.models import Profile
from .models import *
from .forms import CommentForm, CreatePost
from django.db.models import F, Count

# def add_post(request):
#     if request.method == 'POST':
#         form = CreatePost(request.POST, request.FILES)
#         def form_valid(self, form):
#             form.instance.author = self.request.user
#             return super().form_valid(form)
#     else:
#         form = CreatePost()
#     return render(request, 'blog/add_post.html', {'form':form})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','image','category','tags']
    template_name = 'blog/add_post.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','image', 'category','tags',]
    template_name = 'blog/update_post.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Calie'
        return contex


class PostByCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = Category.objects.get(slug=self.kwargs['slug'])
        contex['pop'] = Post.objects.filter(category__slug=self.kwargs['slug']).order_by('-views')
        return contex


class GetPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return contex



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/author.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('slug'))
        return Post.objects.filter(author=user).order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = get_object_or_404(User, username=self.kwargs.get('slug'))
        contex['bio'] = Profile.objects.get(slug=self.kwargs['slug'])
        return contex



def get_author(request, slug):
    return render(request, 'blog/author.html')


def get_tag(request, slug):
    return render(request, 'blog/tag.html')


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        # contex['total_obj'] = Post.objects.count()
        contex['s'] = self.request.GET.get('search')
        contex['search'] = f"search={self.request.GET.get('search')}&"
        return contex


class AddComents(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.post = post
            form.save()
        return redirect(post.get_absolute_url())






