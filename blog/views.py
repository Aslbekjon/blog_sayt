from django.shortcuts import render, redirect
from .models import Blog, Comment, MyUser, Category
from django.views.generic import CreateView
from .forms import BlogForm, CommentForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
# Create your views here.

def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        # "blogs": blogs,
        "blogs": page_obj
    }
    return render(request, "blog.html", context)

def product_search(request):
    results = None
    try:
        query = request.POST['query']
        results = Blog.objects.filter(name__icontains=query) |\
            Blog.objects.filter(description__icontains=query)
        paginator = Paginator(results, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        try:
            results = page_obj

        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:

            results = paginator.page(1)

        wishlist = None
        return render(request,'blog.html', {'blogs': results, 'wishlist': wishlist})
    except KeyError:
        wishlist = None
        "KeyError"
        return render(
            request,
            'blog.html',
            {'blogs': results, 'wishlist': wishlist}
        )

@login_required(login_url='login')
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user
            f.save()
            form.save_m2m()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'blog_create.html', {'form':form})

@login_required(login_url='login')
class BlogCreate(CreateView):
    form_class = BlogForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.user_id = self.request.user

        return super().form_valid(form)

def category_filter(request, slug_category):
    category1 = Blog.objects.filter(category_id__slug = slug_category)
    category_name = Category.objects.get(slug = slug_category)
    paginator = Paginator(category1, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': page_obj,
        'category_name': category_name
    }
    return render(request, "category_filter.html", context)

def category_list(request):
    category = Category.objects.all()
    paginator = Paginator(category, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': page_obj
    }
    return render(request, "category_list.html", context)


def blogDetail(request, slug_name):
    blog = Blog.objects.get(slug=slug_name)
    bogs_author = Blog.objects.filter(user_id=blog.user_id)
    blog_filter_category = Blog.objects.filter(category_id=blog.category_id)[:3]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form_comment = form.save(commit = False)
            form_comment.user_id = request.user
            form_comment.blog_id = blog
            form_comment.save()
            return redirect('detail', slug_name = blog.slug)
    else:
        form = CommentForm()
    blog.views += 1
    blog.save()
    context = {
        'blog': blog,
        'blogs_author': bogs_author,
        'blog_flt_ctry': blog_filter_category,
        'form':form
    }
    return render(request, "detail.html", context)

@login_required(login_url='login')
def blog_update(request, slug_name):
    blog = Blog.objects.get(slug = slug_name)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            # form.save_m2m()
            return redirect('detail', slug_name = blog.slug)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'update_blog.html', {'form': form, 'blog': blog})

@login_required(login_url='login')
def blog_delete(request,slug_name):
    blog = Blog.objects.get(slug=slug_name)
    form = BlogForm(request.POST, instance = blog)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog')
    return render(request, 'delete_blog.html', {'del':blog})

def TagsView(request, slug_tag):
    blogs = Blog.objects.filter(tag__slug = slug_tag)
    return render(request, "blog.html", {'blogs': blogs})