from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect,Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from testapp.models import *
import json
import  os
import  uuid
import  datetime
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.models import User

def test(request):
    return render(request,'test.html')
def index(request):
    return render(request,'index.html')

def login_html(request):
    return render(request,'login.html')

def login_view(request):
    if request.method == 'GET':
        request.session['login_from'] = request.GET.get('next', '/test/index/')
        print(request.session['login_from'])
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                #return HttpResponse('登陆成功')
                request.session['username'] = username
                print(request.session['username'])
                return HttpResponseRedirect(request.session['login_from'])
            else:
                return HttpResponse('登陆失败')
        else:
            return HttpResponse('没有激活')

def logout_view(request):
    logout(request)
    #return render(request,'login.html')
    return HttpResponseRedirect('/test/')#HttpResponseRedirect()后面参数是一个url地址，而不是一个html模板

def change_password(request):
    return HttpResponse('修改成功')

@login_required
def add_case(request,prd_id):
    if request.method == 'GET':
        name=Prd.objects.filter(id=prd_id)[0].name
        print(name)
        return render(request,'addcase.html',{'name':name})
    elif request.method == 'POST':
        req = request.POST
        module = req['module']
        title = req['title']
        content = req['content']
        try:
            p = Prd.objects.filter(id=prd_id)[0]
            u = User.objects.filter(username=request.session['username'])[0]
            Case.objects.get_or_create(prd_name=p, module=module, title=title, content=content,author=u)
            return HttpResponseRedirect('/test/{}/case'.format(prd_id))
        except Exception as e:
            return HttpResponse('创建失败')

@login_required
def add_prd(request):
    if len(request.POST) == 0:
        return render(request,'addprd.html')
    else:
        req = request.POST
        name = req['name']
        prd_url = req['prd_url']
        try:
            Prd.objects.create(name=name, prd_url=prd_url)
            return HttpResponseRedirect('/test/prd/')
        except Exception as e:
            return HttpResponse('创建失败')

@login_required
def add_article(request):
    if len(request.POST) == 0:
        return render(request,'addarticle.html')
    else:
        req = request.POST
        title = req['title']
        keyword = req['keyword']
        content = req['content']
        author_id = User.objects.filter(username=request.session['username'])[0].id
        try:
            Article.objects.create(title=title, keyword=keyword,content=content,author_id=author_id)
            return HttpResponseRedirect('/test/article/all/')
            #messages.add_message(request,messages.SUCCESS,'创建成功！')
        except Exception as e:
            return HttpResponse('创建失败')

def get_case_list(request,prd_id):
    case_list=Case.objects.filter(prd_name_id=prd_id).order_by('id')
    return render(request,'caselist.html',{'case_list':case_list,'len':len(case_list),'prd_id':prd_id})

def get_prd_list(request):
    prd_list=Prd.objects.all()
    return render(request,'prdlist.html',{'prd_list':prd_list,'len':len(prd_list)})

def get_article_list(request):
    article_list=Article.objects.all()
    return render(request,'articlelist.html',{'article_list':article_list,'len':len(article_list)})

def get_personal_article_list(request,author):
    author_id = User.objects.filter(username=author)[0].id
    article_list = Article.objects.filter(author_id=author_id).order_by('id')
    return  render(request,'articlelist.html',{'article_list':article_list,'len':len(article_list)})

def case_detail(request,case_id):
    try:
        case = Case.objects.get(id=case_id)
        id = Prd.objects.filter(id=case.prd_name_id)[0].id
        return render(request, 'casedetail.html', {'case': case,'id':id})
    except Case.DoesNotExist:
        raise Http404

@login_required
def change_case(request,case_id):
    if len(request.POST)==0:
        try:
            case = Case.objects.get(id=case_id)
            name = Prd.objects.filter(id=case.prd_name_id)[0].name
            return render(request, 'changecase.html', {'case': case, 'name': name})
        except Case.DoesNotExist:
            raise Http404
    else:
        module = request.POST['module']
        title = request.POST['title']
        content = request.POST['content']
        Case.objects.filter(id=case_id).update(module=module,title=title,content=content)
        return HttpResponseRedirect('/test/case/{}/'.format(case_id))


def delete_case(request,case_id):
    try:
        c=Case.objects.filter(id=case_id)
        prd_id=c[0].prd_name_id
        print(prd_id)
        Case.objects.filter(id=case_id).delete()
        return HttpResponseRedirect('/test/{}/case'.format(prd_id))
    except Exception as e:
        return HttpResponse('删除失败')

@login_required
def delete_article(request,article_id):
    try:
        Article.objects.filter(id=article_id).delete()
        return JsonResponse('删除成功',safe=False)
    except Exception as e:
        return HttpResponse(json.dump('删除失败'))

def change_prd(request,prd_id):
    if request.method == 'GET':
        try:
            prd = Prd.objects.get(id=prd_id)
            return render(request, 'changeprd.html', {'prd':prd})
        except Case.DoesNotExist:
            raise Http404
    else:
        name = request.POST['name']
        prd_url = request.POST['prd_url']
        Prd.objects.filter(id=prd_id).update(name=name,prd_url=prd_url)
        return HttpResponseRedirect('/test/prd/')

def article_detail(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
        return render(request, 'articledetail.html', {'article': article})
    except Case.DoesNotExist:
        raise Http404
def change_article(request,article_id):
    if len(request.POST)==0:
        try:
            article = Article.objects.get(id=article_id)
            return render(request, 'changearticle.html', {'article':article})
        except Case.DoesNotExist:
            raise Http404
    else:
        title = request.POST['title']
        keyword = request.POST['keyword']
        content = request.POST['content']
        Prd.objects.filter(id=article_id).update(title=title,keyword=keyword,content=content)
        return HttpResponse('更新成功')

def search(request):
    keyword = request.POST['keyword']
    prd_result=Prd.objects.filter(name__contains=keyword)
    article_title_result = Article.objects.filter(title__contains=keyword)
    #print (type(article_title_result))
    #article_keyword_result = Article.objects.filter(keyword__contains=keyword)
    #article_result = list(set(article_title_result+article_keyword_result))
    return render(request,'result.html',{'prd_result':prd_result,'article_result':article_title_result})



'''
@csrf_exempt用于取消csrftoken验证
url为:http://127.0.0.1:8000/admin/upload/?dir=media post请求
'''
@csrf_exempt
def upload(request):
    '''
    kindeditor图片上传返回数据格式说明：
    {"error": 1, "message": "出错信息"}
    {"error": 0, "url": "图片地址"}
    '''
    result = {"error": 1, "message": "上传失败"}
    files = request.FILES.get("imgFile", None)  #input type="file" 中name属性对应的值为imgFile
    type = request.GET['dir']  #获取资源类型
    if  files:
        result = process_upload(files,type)
        print(result)
    #结果以json形式返回
    return HttpResponse(json.dumps(result),content_type="application/json")

def is_ext_allowed(type,ext):
    '''
    根据类型判断是否支持对应的扩展名
    '''
    ext_allowed = {}
    ext_allowed['image'] = ['jpg','jpeg', 'bmp', 'gif', 'png']
    ext_allowed['flash'] = ["swf", "flv"]
    ext_allowed['media'] = ["swf", "flv", "mp3", "wav", "wma", "wmv", "mid", "avi", "mpg", "asf", "rm", "rmvb", "mp4"]
    ext_allowed['file'] = ["doc", "docx", "xls", "xlsx", "ppt", "htm", "html", "txt", "zip", "rar", "gz", "bz2", 'pdf']
    return ext in ext_allowed[type]

def get_relative_file_path():
    '''
    获取相对路径
    '''
    dt = datetime.datetime.today()
    relative_path = 'upload/%s/%s/' %(dt.year,dt.month)
    absolute_path = os.path.join(settings.MEDIA_ROOT,relative_path)
    print('BASE_DIR:',settings.BASE_DIR)
    print('settings.MEDIA_ROOT:',settings.MEDIA_ROOT)
    print('1:',absolute_path)
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)
    return relative_path

def process_upload(files,type):
    dir_types = ['image','flash','media','file']
    #判断是否支持对应的类型
    if type not in dir_types:
        return {"error":1, "message": "上传类型不支持[必须是image,flash,media,file]"}

    cur_ext = files.name.split('.')[-1]  #当前上传文件的扩展名
    #判断是否支持对应的扩展名
    if not is_ext_allowed(type,cur_ext):
        return {'error':1, 'message': 'error:扩展名不支持 %s类型不支持扩展名%s' %(type,cur_ext)}

    relative_path = get_relative_file_path()
    print('2:',relative_path)
    #linux中一切皆文件
    file_name = str(uuid.uuid1()) + "." + cur_ext
    base_name = os.path.join(settings.MEDIA_ROOT,relative_path)
    print(base_name)
    file_full_path = os.path.join(base_name,file_name).replace('\\','/') #windows中的路径以\分隔
    print('file_full_path:',file_full_path)
    file_url = settings.MEDIA_URL + relative_path + file_name
    print('file_url',file_url)
    with open(file_full_path,'wb') as f:
        if  files.multiple_chunks() == False:  #判断是否大于2.5M
            f.write(files.file.read())
        else:
            for chunk in files.chunks():
                f.write(chunk)
    return {"error": 0, "url": file_url}

def pay_flow(request):
    import requests
    mid=request.POST['mid']
    dts=request.POST['dts']
    dte = request.POST['dte']
    url='http://61.141.235.66:36128/api/qo'
    data=request.get(url,)


