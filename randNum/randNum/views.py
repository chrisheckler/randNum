from django.http import HttpResponse
import random
from django.utils.html import escape
import requests


def rand_num(request):
    #panda()
    #rand = random.randint(0, 100)
    #rand = fib(rand)
    #request_introspect = repr(request)
    #html = "<html><body>Magic number of the day is: %f</body></html>" % rand
    #html = "<html><body> %s</body></html>" % request
    #return HttpResponse(html)
    #ireturn HttpResponse(escape(repr(request)))
    #fib_num = fib(int(request.GET.get('q', '')))
    #html = "<html><body> %d</body></html>" % fib_num
    html = "<html><body> %d</body></html>" % fib(10) 
    return HttpResponse(html)


def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b=b,b+a
    return b


def panda():
    for i in range(1):
        requests.get("http://127.0.0.1:8000/rnum/q=%d" % i) 
