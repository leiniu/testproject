from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from testapp.models import *
from django.http import Http404

def index(request):
    return render(request,'index.html')

def login_html(request):
    return render(request,'login.html')
def login(request):
    u = User.objects.filter(username=request.POST['username'])
    if len(u) == 0:
        return  HttpResponse('用户名不存在，请联系管理员添加。')
    else:
        m = u[0]
        if m.password == request.POST['password']:
            request.session['username'] = request.POST['username']
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Your username and password didn't match.")

def addcase(request):
    if len(request.POST) == 0:
        prd_lists=Prd.objects.all()
        return render(request,'addcase.html',{'prd_lists':prd_lists})
    else:
        req = request.POST
        prd_name = req['prd_name']
        module = req['module']
        title = req['title']
        content = req['content']
        print(content)
        try:
            p = Prd.objects.filter(id=int(prd_name))[0]
            print(p.name)
            Case.objects.create(prd_name=p, module=module, title=title, content=content)
            return HttpResponse('创建成功')
        except Exception as e:
            return HttpResponse('创建失败')

def addprd(request):
    if len(request.POST) == 0:
        return render(request,'addprd.html')
    else:
        req = request.POST
        name = req['name']
        prd_url = req['prd_url']
        try:
            Prd.objects.create(name=name, prd_url=prd_url)
            return HttpResponse('创建成功')
        except Exception as e:
            return HttpResponse('创建失败')

def get_list(request):
    return render(request,'case-list.html')
def get_case_list(request,prd_id):
    case_list=Case.objects.filter(prd_name_id=prd_id).order_by('id')
    return render(request,'caselist.html',{'case_list':case_list,'len':len(case_list)})

def get_prd_list(request):
    prd_list=Prd.objects.all()
    return render(request,'prdlist.html',{'prd_list':prd_list,'len':len(prd_list)})

def get_article_list(request,author):
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
        return HttpResponse('更新成功')

def change_prd(request,prd_id):
    if len(request.POST)==0:
        try:
            prd = Case.objects.get(id=prd_id)
            return render(request, 'changeprd.html', {'prd':prd})
        except Case.DoesNotExist:
            raise Http404
    else:
        name = request.POST['name']
        prd_url = request.POST['prd_url']
        Prd.objects.filter(id=prd_id).update(name=name,prd_url=prd_url)
        return HttpResponse('更新成功')

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
