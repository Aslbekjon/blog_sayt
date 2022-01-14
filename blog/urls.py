from django.urls import path
from .views import blog,blogDetail,product_search, TagsView, category_filter, category_list, blog_create, blog_update, blog_delete
from .views import BlogCreate

urlpatterns = [
    path('', blog, name="blog"),
    path('search', product_search, name='product_search'),
    path('detail/<slug:slug_name>', blogDetail, name="detail"),
    path('tags/<slug:slug_tag>', TagsView, name='tags'),
    path('category/<slug:slug_category>', category_filter, name='category'),
    path('blog_create', blog_create, name="blog_create"),
    # path('blog_create', BlogCreate.as_view(), name="blog_create"),
    path('category_list', category_list, name="category_list"),
    path('update/<slug:slug_name>', blog_update, name="update"),
    path('delete/<slug:slug_name>', blog_delete, name="delete")

]