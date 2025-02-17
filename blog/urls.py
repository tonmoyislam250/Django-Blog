from django.conf.urls import url

from blog.views import display_post, delete_post, display_posts, print_post, PostCreateView, PostUpdateView, print_preview, add_comment

urlpatterns = [
    url(r'^posts/$', display_posts, name="DisplayPosts"),
    url(r'^posts/create/$', PostCreateView.as_view(), name="CreatePost"),
    url(r'^post/delete/$', delete_post, name="DeletePost"),
    url(r'^post/(?P<post_id>\d+)/$', display_post, name="DisplayPost"),
    url(r'^post/(?P<post_id>\d+)/update/$', PostUpdateView.as_view() , name="UpdatePost"),
    url(r'^post/(?P<post_id>\d+)/print/$', print_post, name="PrintPost"),
    url(r'^post/(?P<post_id>\d+)/preview/$', print_preview, name="PrintPreview"),
    url(r'^post/(?P<post_id>\d+)/comment/$', add_comment, name='AddComment')
]
