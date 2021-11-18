from django.shortcuts import render

def blog(request):
	var = {'title': 'tomiblog', 'file': ["[y]test", "[b]test2", "[y]test3"]}
	return (render(request, 'blog/main.html', var))
