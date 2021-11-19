from django.shortcuts import render
from html import escape
from .models import Article

def blog(request, page):
	content = Article.objects.all()[page*10:(page*10)+10]
	var = {'title': 'tomiblog', 'file': ["[y]test", "[b]test2", "[y]test3"], 'articles': content}
	return (render(request, 'blog/blog.html', var))
