from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView,View,UpdateView
from .models import Comment,Liked,Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from .forms import CommentForm
from .models import Comment,Blog

# Create your views here.



class Blog_list_page(ListView):
    template_name = 'App_Blog/blog_list.html'
    model = Blog
    context_object_name = 'blogs'
    queryset = Blog.objects.order_by('-pub_date')

class MyBlog_list(LoginRequiredMixin,ListView):

    model = Blog
    template_name = 'App_Blog/my_block.html'

class UpdateBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ('blog_title','blog_contant','blog_images')
    template_name = 'App_Blog/edit_block.html'

    def get_success_url(self,**kwargs):
        return reverse_lazy('Blog:detail_blog',kwargs={'slug':self.object.slug})




class CreatBlock(LoginRequiredMixin,CreateView):

    model = Blog
    fields = ('blog_title','blog_contant','blog_images')
    template_name = 'App_Blog/create_block.html'

    def form_valid(self, form):
        blog_obj=form.save(commit=False)
        blog_obj.author=self.request.user
        title=blog_obj.blog_title
        blog_obj.slug=title.replace(' ','-')+'-'+str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

@login_required(login_url='/')
def Detailblockfunc(request,slug):
    blog=Blog.objects.get(slug=slug)
    com=Comment.objects.filter(blog=blog)
    all_liked=Liked.objects.filter(blog=blog)
    form=CommentForm()
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.blog=blog
            obj.user=request.user
            obj.save()
            return HttpResponseRedirect(reverse('Blog:detail_blog',kwargs={'slug':slug}))
    return render(request,'App_Blog/blog_detail.html',context={'blog':blog,'form':form,'com':com,'all_liked':len(all_liked)})

def likefunction(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    all_like= Liked.objects.all()
    already_like=Liked.objects.filter(blog=blog,user=user)
    if len(already_like)==0:
        like=Liked(blog=blog,user=user)
        like.save()
    if len(already_like)==1:
        already_like.delete()
    return HttpResponseRedirect(reverse('Blog:detail_blog',kwargs={'slug':blog.slug}))


def dislikefunc(request,pk):
    pass

# class DeleteMycomment(DeleteView):
#     model = Comment
#     context_object_name = 'delet_comment'
#     template_name = 'App_Blog/delete_comment.html'
#     success_url = reverse_lazy('index')

def DeleteMycomment(request,pk):
    delete_c=Comment.objects.get(pk=pk)
    if request.method== 'POST':
        delete_c.delete()
        return HttpResponseRedirect(reverse('Blog:detail_blog',kwargs={'slug':delete_c.blog.slug}))
    return render(request,'App_Blog/delete_comment.html',context={'ff':delete_c})

