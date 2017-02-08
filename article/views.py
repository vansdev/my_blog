from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from article.models import Article


def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})


def detail(request,args):
    post = Article.objects.all()[int(args)]
    str = ('title = %s, category = %s date_time = %s content = %s' % (post.title,post.category,post.date_time,post.content))
    return HttpResponse(str)