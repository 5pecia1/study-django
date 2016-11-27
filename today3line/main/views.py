from django.shortcuts import render
from django.http import HttpResponse

def index(reg) :
    return render(reg, 'main/index.html') # render는 자신의 경로에서 templates이라는 폴더를 찾는다.
