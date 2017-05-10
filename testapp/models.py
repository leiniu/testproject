from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class User (models.Model):
    username=models.CharField('用户名',max_length=10)
    password=models.CharField('密码',max_length=20)

    def __str__(self):
        return self.username

class Prd (models.Model):
    name = models.CharField('需求名称',max_length=256)
    prd_url = models.CharField('需求地址',default='',max_length=256)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('prd',args=(self.id,))

    class Meta:
        verbose_name='需求名称'
        verbose_name_plural = '需求名称'

class Case (models.Model):
    prd_name = models.ForeignKey(Prd)
    author = models.ForeignKey(User)
    module = models.CharField('模块',max_length=256)
    title = models.CharField('标题',max_length=256)
    content = models.TextField('内容',default='',blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        print (self.id)
        return reverse('case_detail',args=(self.id,))
    class Meta:
        verbose_name = '用例'
        verbose_name_plural = '测试用例'

class Article(models.Model):
    title =  models.CharField('文章标题',max_length=50)
    keyword = models.CharField('关键字',max_length=256)
    author = models.ForeignKey(User)
    content = models.TextField('内容',default='',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章'