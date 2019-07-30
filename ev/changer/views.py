import json

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import main

sentiment_analysis = main.Sentiment_analysis()
#여기서 다 만들어 놓고


# sentence, score = sentiment_analysis.Sentiment_analysis_predict_pos_neg("아 왜 이렇게 느려 짜증나게")

# Create your views here.
# 테스트용 메인 페이지
def index(request):
    return HttpResponse("Hello world, comment changer's indexing page.")

# test용 페이지.
def changer(request):
    return HttpResponse("Hello")

# 테스트용으로 임시로 만들어둔 POST를 받는 부분
# number의 URL로 POST를 전송하면 데이터를 받아서 템플릿을 통해 다시 가공된 데이터를 전송함.


@csrf_exempt
def comment(request):
    info = request.POST['commentContent']
    sentence ,score = sentiment_analysis.Sentiment_analysis_predict_pos_neg(info)
    ##  가공된 데이터를 render하지만, 자동으로 상대에게 form 전송 action이 취해짐.
    # #return render_to_response('changer/post.html',{'comment':sentence,'score':score})
    return HttpResponse(str(score))
