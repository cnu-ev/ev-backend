from django.db import models
from django.urls import reverse

from django.conf import settings

# Create your models here.

# 글쓰기에 관한 모델 Post
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True,
                                   help_text='simple description text')  # 간단한 설명
    content = models.TextField('CONTENT')  # 본문 내용( 여러 줄 가능 )
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    post_writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    emotion_propotion = models.BigIntegerField('Emotion Propotion', default=0)


    # 필드 속성 외에 필요한 파라미터를 Meta 내부 클래스로 정의 가능
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_post'  # db에 저장되는 table 이름
        ordering = ('-modify_date',)

    # 객체의 문자열 표시를 정의합니다.(=toString)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null=True, related_name = 'comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    emotion_propotion = models.BigIntegerField('Emotion Propotion',default=0)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        db_table = 'blog_comment'  # db에 저장되는 table 이름
        ordering = ['-id']


