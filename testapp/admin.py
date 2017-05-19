from django.contrib import admin
from .models import Case,Prd,User,Article

class CaseAdmin(admin.ModelAdmin):
    list_display = ('title','prd_name','module','content',)
    
    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'js/editor/kindeditor/kindeditor-all.js',
            'js/editor/kindeditor/lang.zh_CN.js',
            'js/editor/kindeditor/config.js',
        )

class PrdAdmin(admin.ModelAdmin):
    list_display = ('name','prd_url',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','keyword','author',)

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'js/editor/kindeditor/kindeditor-all.js',
            'js/editor/kindeditor/lang.zh_CN.js',
            'js/editor/kindeditor/config.js',
        )
admin.site.register(Case,CaseAdmin)
admin.site.register(Prd,PrdAdmin)
admin.site.register(Article,ArticleAdmin)

