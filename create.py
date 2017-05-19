'''
create some records for demo database
'''

from testproject.wsgi import *
from testapp.models import Case,Prd
'''
def main():
    prd_urls = [
        ('银联二维码', '123456'),
        ('刷宝', 'qwertyuu'),
        ('需求3','sdfdkfjdsk f'),
        ('需求4','skmvccbn f'),
    ]

    for x, y in prd_urls:
        p = Prd.objects.get_or_create(name=x, prd_url=y)[0]
        print(1)

        for i in range(1,10):
            
            c = Case.objects.get_or_create(prd_name=p,module=x, title='{}_{}_{}'.format(x,'用例',i),content='思考大幅减少旅客谨防三大框架富士康')[0]
            print(2)
            #c.prd_name.add(p)
'''





if __name__ == '__main__':
    main()
    print("Done!")