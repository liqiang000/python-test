def demo(a,b):
    print(a+b)
demo(1,2)

def demo1(a,b=2):
    print(a+b)
demo1(3)
demo1(3,3)

#不定长参数 *代表一个参数，** 代表k v参数
def function(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(*args)
    for i in kwargs.items():
        print(i)
function(1,2,3,4,5,m=7,n=8,k=9)


def add(a):
    a+=a
    print(a)
#a=10  #不可变参数
a=[1,2]
add(a)
print(a)