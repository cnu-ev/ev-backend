import json

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
import urllib
import urllib3

# Create your views here.
# 테스트용 메인 페이지
def index(request):
    return HttpResponse("Hello world, it's django")

# test용 페이지.
def changer(request):
    return HttpResponse("Hello")

# 테스트용으로 임시로 만들어둔 POST를 받는 부분
# number의 URL로 POST를 전송하면 데이터를 받아서 템플릿을 통해 다시 가공된 데이터를 전송함.
def number(request):
    info = request.POST['info']
    # 가공된 데이터를 render하지만, 자동으로 상대에게 form 전송 action이 취해짐.
    return render_to_response('changer/post.html',{'comment':info})