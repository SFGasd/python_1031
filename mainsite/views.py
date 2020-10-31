from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.

def index(request):
    now_date = datetime.now
    lucky_nums = list()
    lucknum = random.randint(1, 42)
    for i in range(6):
        lucky_nums.append(random.randint(1, 42))
    return render(request, 'index.html', locals())