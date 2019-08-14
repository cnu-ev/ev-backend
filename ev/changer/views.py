import json

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from django.utils.html import strip_tags

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
    soup = BeautifulSoup(info)
    text = soup.get_text()


    data_sentence = strip_tags(text)
    sentence ,score = sentiment_analysis.Sentiment_analysis_predict_pos_neg(data_sentence)
    ##  가공된 데이터를 render하지만, 자동으로 상대에게 form 전송 action이 취해짐.
    # #return render_to_response('changer/post.html',{'comment':sentence,'score':score})
    return HttpResponse(str(score))

@csrf_exempt
def review(request):
    reviewScore = request.POST['IsPositive']
    reviewComment = request.POST['CommentContent']

    count = 0
    with open('/home/radi/ev-backend/ev/changer/review.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            count += 1
    f.close()

    count += 1
    count = repr(count)

    f2 = open("/home/radi/ev-backend/ev/changer/review.txt","a")
    f2.write("\n"+count+"\t"+reviewComment+"\t"+reviewScore)
    f2.close()

    return HttpResponse("리뷰가 전송되었습니다.")