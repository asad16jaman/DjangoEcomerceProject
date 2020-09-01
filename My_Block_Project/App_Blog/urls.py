from django.urls import path
from . import views
app_name='Blog'

urlpatterns=[
    path('',views.Blog_list_page.as_view(),name='blog_list'),
    path('create/',views.CreatBlock.as_view(),name='create_block'),
    path('detail/<str:slug>/',views.Detailblockfunc,name='detail_blog'),
    path('liked/<int:pk>/',views.likefunction,name='liked'),
    path('dislike/<int:pk>/',views.dislikefunc,name='dislike'),
    path('my-blog/',views.MyBlog_list.as_view(),name='my_blog'),
    path('edit-blog/<pk>/',views.UpdateBlog.as_view(),name='edit_blog'),
    path('delete-comment/<pk>/',views.DeleteMycomment,name='delete_comment'),
]