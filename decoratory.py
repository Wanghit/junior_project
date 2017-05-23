#-*-enconding=UTF-8-*-
def log(*args,**kwargs):
  def inner(func):
      #*no name
      #** have name
    def wrapper(*args,**kwargs):
        print 'before calling',func.__name__
        func(*args,**kwargs)
        print 'end calling',func.__name__
    return wrapper
  return inner
@log(level='INFO')
def hello():
    print 'hello'
@log(level='INFO')
def hello2(name):
    print 'hello',name

if __name__=='__main__':
    #hello()
     hello2('name')
     hello()