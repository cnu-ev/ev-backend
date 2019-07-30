# ev-backend
## CNU CSE Bottom-Up Project Team-Ev
 분석사이트를 제작하는 Team-Ev의 backend repository 입니다.  
 Django를 기반으로 제작되었으며, konlpy와 tensorflow 를 기반으로 하는 감정분석 판별기를 포함합니다.
 
 ## How to Use
 ##### FrontServer에서 /changer/comment url로 Post를 날리면, 해당 POST를 request에서 읽어와, 미리 생성된 감정분석 모델에 대입, 부정 및 긍정의 수치를 score의 형태로 다시 HttpResponse합니다. Front에서는 이 Score 데이터를 기반으로 댓글을 감정에 기반한 시각화 작업을 실시하게 됩니다.
 

### Environment
> Elementary OS 5.0 (based on Ubuntu 18.04.2)  
> Linux 4.15.0-54-generic  
> python3.6.8  



### Requirements
```
absl-py==0.7.1
astor==0.8.0
boto==2.49.0
boto3==1.9.194
botocore==1.12.194
certifi==2019.6.16
chardet==3.0.4
Django==2.0.13
django-cors-headers==3.0.2
docutils==0.14
gast==0.2.2
gensim==3.8.0
google-pasta==0.1.7
grpcio==1.22.0
h5py==2.9.0
idna==2.8
jmespath==0.9.4
joblib==0.13.2
JPype1==0.7.0
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
konlpy==0.5.1
Markdown==3.1.1
mecab-python==0.996
numpy==1.16.4
pkg-resources==0.0.0
protobuf==3.9.0
pybind11==2.3.0
python-dateutil==2.8.0
pytz==2019.1
requests==2.22.0
s3transfer==0.2.1
scikit-learn==0.21.2
scipy==1.3.0
six==1.12.0
smart-open==1.8.4
tensorboard==1.14.0
tensorflow==1.14.0
tensorflow-estimator==1.14.0
termcolor==1.1.0
urllib3==1.25.3
uWSGI==2.0.18
Werkzeug==0.15.5
wrapt==1.11.2


```
