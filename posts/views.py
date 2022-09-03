from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.http import Http404
from django.db.models import Count

from datetime import datetime, timedelta
from collections import OrderedDict

from .models import Post, Tag, Category
from accounts.models import CustomUser as Author

from .forms import PostForm


# TODO: separate of menu and columns loader from main views


class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'
    context_object_name = 'posts'

    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        # posts
        all_posts = Post.objects

        ordered_posts = all_posts.order_by('created_at')
        dates_list = []
        for post in ordered_posts:
            month_date = post.created_at.strftime(r"%b-%Y")
            if month_date not in dates_list:
                dates_list.append(month_date)
        context['pub_months'] = dates_list

        # top posts
        top_posts = all_posts.order_by('-counter')
        context['top_posts'] = top_posts[:5]

        top_authors = Author.objects.all().annotate(num_posts=Count('post')).order_by('-num_posts')
        context['top_authors'] = top_authors[:5]

        top_categories = Category.objects.all().annotate(num_posts=Count('post')).order_by('-num_posts')
        context['top_categories'] = top_categories[:5]

        top_tags = Tag.objects.all().annotate(num_posts=Count('post')).order_by('-num_posts')
        context['top_tags'] = top_tags[:5]

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        # posts
        all_posts = Post.objects

        # get next and previous posts
        post_slug = self.kwargs['slug']
        current_post = all_posts.filter(slug=post_slug).first()

        # add one to counter
        current_post.counter = current_post.counter+1
        current_post.save()

        # activate after launch :D
        '''
        if current_post.state != Post.STATES.PUBLISHED:
            raise Http404('Post does not exist!')
        '''

        post_id = current_post.pk

        next_post_id = post_id+1
        previous_post_id = post_id-1

        next_post = Post.objects.filter(id=next_post_id).first()
        previous_post = Post.objects.filter(id=previous_post_id).first()

        context['next_post'] = next_post
        context['previous_post'] = previous_post

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/create.html'
    context_object_name = 'post'
    #fields = ['title', 'state', 'categories', 'tags', 'content']
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post/update.html'
    context_object_name = 'post'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        request.POST = request.POST.copy()
        if 'change_slug' in request.POST.keys():
            # TODO: change slug after update
            print('slug slug')
        return super(PostUpdateView, self).post(request, **kwargs)

    def test_func(self):
        # TODO: add user groups
        obj = self.get_object()
        return True
        return obj.user == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        # TODO: add user groups
        obj = self.get_object()
        return True
        return obj.user == self.request.user


class PostMonthView(ListView):
    model = Post
    template_name = 'post/month.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        inputs = self.kwargs['month'].split('-')
        try:
            month_date = datetime.strptime(f'{inputs[0]}-{inputs[1]}', '%b-%Y').date()
            queryset = Post.objects.filter(created_at__year=month_date.year, created_at__month=month_date.month)
            return queryset
        except:
            raise Http404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostMonthView, self).get_context_data(**kwargs)
        inputs = self.kwargs['month'].split('-')
        try:
            month_date = datetime.strptime(f'{inputs[0]}-{inputs[1]}', '%b-%Y').date()
            context['month'] = month_date
            return context
        except:
            raise Http404


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'categories'

    paginate_by = 10


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = 'category'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category/create.html'
    context_object_name = 'category'
    fields = ['name', ]
    '''
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)'''


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    template_name = 'category/update.html'
    context_object_name = 'category'
    fields = ['name', ]

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        request.POST = request.POST.copy()
        if 'change_slug' in request.POST.keys():
            # TODO: change slug after update
            print('slug slug')
        return super(CategoryUpdateView, self).post(request, **kwargs)

    def test_func(self):
        # TODO: add user groups
        obj = self.get_object()
        return True
        return obj.user == self.request.user


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category/delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        # TODO: add user groups
        obj = self.get_object()
        return True
        return obj.user == self.request.user


class TagListView(ListView):
    model = Tag
    template_name = 'tag/list.html'
    context_object_name = 'tags'
    paginate_by = 25


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag/detail.html'
    context_object_name = 'tag'


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'tag/create.html'
    context_object_name = 'tag'
    fields = ['name', ]
    '''
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)'''


class TagUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tag
    template_name = 'tag/update.html'
    context_object_name = 'tag'
    fields = ['name', ]

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        request.POST = request.POST.copy()
        if 'change_slug' in request.POST.keys():
            # TODO: change slug after update
            print('slug slug')
        return super(TagUpdateView, self).post(request, **kwargs)

    def test_func(self):
        # TODO: add user groups
        obj = self.get_object()
        return True
        return obj.user == self.request.user


class TagDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tag
    template_name = 'tag/delete.html'
    context_object_name = 'tag'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        # TODO: add user groups
        obj = self.get_object()
        return True
        return obj.user == self.request.user


class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'
    context_object_name = 'authors'
    paginate_by = 25


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/detail.html'
    context_object_name = 'author'

