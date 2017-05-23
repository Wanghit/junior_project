import random
import re
def demo_string():
    str='hello world'
    print str
    print str.capitalize()
    print 1,str
    print str.startswith('he')
    print str.replace('worl','newcode')
    print str.endswith('x')
    sta='ssssfsd\n'
    #print sta.lstrip()
    #print sta.rstrip()
    print str+sta
    print 6,len(str)
    print 7,'-'.join(['a','b','c'])
    print 8,str.split(' ')
    print 9,str.find('ell')
def demo_operation():
    print 1,1+2,5/2,5*2,5-2
    print 2,True,not True
    print 3,1<2,5>3
    print 4,2<<3
    print 5,5|3,5&3,5^3
    x=2
    y=3.3
    print x,y,type(x),type(y)
def demo_buildinfunction():
    print 1,max(2,1),min(3,1)
    print 2,len('xxx'),len([1,2,3])
    print 3,abs(-2)
    print 4,range(1,10,3)
    print 5,dir(list)
    x=2
    print 6,eval('x+3')
    print 7,chr(97),ord('a')
    print 8,divmod(3,2)
def demo_controlflow():
    score=65
    if score>99:
        print 1,'A'
    elif score>60:
        print 2,'B'
    else:
        print  3,'C'
    while score<100:
        print score
        score+=10
    score=65
    for i in range(0,10,2):
        if i==0:
            pass
        if i<5:
            continue
        if i>6:
            break
        print 3,i
def demo_list():
    lista=[1,2,'a']
    listb=[3,4,5]
    print 1,lista
    print 2,listb
    lista.extend(listb)
    print 3,lista
    print 4,len(lista)
    print 5,'a' in lista
    listb.insert(0,'www')
    listb.pop(1)
    print 8,listb
    listb.reverse()
    print 9,listb
    print 10,listb[0],listb[1]
    listb.sort()
    print 11,listb
    listb.sort(reverse=True)
    print listb
    print 13,listb*2
    print 14,[0]*3
    listb.append(4)
    print 15,listb
    tuple=(1,2,3)
    print tuple.index(1)
def demo_dict():
    dict={1:1,2:4,3:9}
    print 1,dict
    print 2,dict.keys(),dict.values()
    print dict.has_key(1),dict.has_key(3)
    for key,value in dict.items():
        print key,value
    dictb={'+':add,'-':sub}
    print 4,dictb['+'](1,2)
    print 5,dictb.get('-')(15,3)
    dictb['*']='x'
    print dictb
    dict.pop(1)
    print dict
    del dict[2]
    print 3,dict

def add(a,b):
    return  a+b
def sub(a,b):
    return  a-b
def demo_set():
    seta=set((1,2,3))
    setb=set((2,3,4))
    print 1,seta
    print 2,seta
    print 3,seta.intersection(setb),seta&setb
    print 4,setb|seta,seta.union(setb)
    print 5,seta-setb
    seta.add('x')
    print 6,seta
    print len(seta)
class User:
    type='USER'
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def __repr__(self):
        return  'im '+self.name+' '+str(self.uid)
class Admin(User):
    type = 'ADMIN'
    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)
        self.group=group
    def __repr__(self):
        return 'im '+self.name+' '+str(self.uid)+' '+self.group
class Guest(User):
    type = 'GUEST'
    def __repr__(self):
        return 'im guest '+self.name+' '+str(self.uid)

def create_user(type):
    if type=='USER':
        return User('u1',1)
    elif type=='ADMIN':
        return Admin('a1',101,'g1')
    elif type == 'GUEST':
        return Guest('a1', 101)
    else:
        raise ValueError('error')
def demo_exception():
    try:
        print 2/1
        #print 2/0
        raise Exception('Raise Error','NowCoder')
    except Exception as e:
        print 'error:',e
    finally:
        print 'clean up'
def demo_randow():
    #random.seed(1)
    print 1,int(random.random()*100)
    print 2,random.randint(0,100)
    print 3,random.choice(range(0,100))
    print 4,random.sample(range(0,100),4)
    a=[1,2,3,4,5]
    random.shuffle(a)
    print 5,a
def demo_re():
    str='abc123def12gewu132'
    pl=re.compile('\D+')
    p2=re.compile('\d')
    print 1,pl.findall(str)
    print 2,p2.findall(str)
    str='a@163.com;b@gmail.com;c@163.com;d@qq.com'
    p3=re.compile('\w+@[163|qq]+\.com')
    print 3,p3.findall(str)
    str='<html><h>title</h><body>xxx</body></html>'
    p4=re.compile('<h>[^<]+</h>')
    print 4,p4.findall(str)
    p4=re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5,p4.findall(str)
    str='xx2016-12-16;2016-11-1'
    p5=re.compile('\d\d\d\d-\d\d-\d\d')
    print 6,p5.findall(str)
    p6 = re.compile('\d{4}-\d{2}-[\d\{2\}]')
    print 7, p6.findall(str)
if __name__=='__main__':
     '''
       user1=User('u1',1)
       print user1
       admin1=Admin('a1',101,'g1')
       print admin1
       print create_user('GUEST')
     '''
      #demo_exception()
      #demo_string()
      #demo_operation()
      #demo_buildinfunction()
      #demo_controlflow()
      #demo_list()
      #demo_dict()
      #demo_set()
      #demo_randow()
     demo_re()
