from django.http import HttpResponse
import random

def rand_num:
    rand = random.randint(0, 100)
    html = "<html><body>Magic number of the day is: " + rand
    return HttpResponse(html)
