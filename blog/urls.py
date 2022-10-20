from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from .views import AddPostView

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('upload/', views.image_upload_view),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
