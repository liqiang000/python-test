# a=["a","b","c","d"]
# b=["a1","b2","c3","d4"]
# c=["a1","b2","c3","d4"]
# e=[1,3,4,5,6,6,7,8,8,99,00]
# print(a)
# a.append("e")
# print(a)
# b.extend(a)
# print(b)
# print(a)
# a.extend(b)
# print(a)
# a.insert(2,100)  #在位置2前边增加
# print(a)
#
# print("*"*50)
# print(a)
# #del(c)
# a.pop()
# print(a)
# c.remove("a1")
# print(c)
# #c.clear()
#
# print(c)
#
#
# # 集合set 是一个无序 不重复的序列
# d=set('abcdefg')
# print(d)
# d.add("r") #默认在最后添加
# print(d)
#
# thisset = set(("Google", "Runoob", "Taobao"))
# print(thisset)
# thisset.update({1,2,3})  #也可以添加元素，且参数可以是列表，元组，字典等
# print(thisset)
# thisset.update([1,9],[2,6],[4,5]) #增加列表
# print(thisset)
# thisset.remove(3)
# print(thisset)
# thisset.discard(5) #移除集合中的元素，且如果元素不存在，不会发生错误
# print(thisset)
# e.sort()
# print(e)
# e.reverse()  #反转
# print(e)
# for i,j in enumerate(e):  #打印索引和值
#     print("%d---%d"%(i,j))
#
#
# #元组使用小括号不能修改值

a=(1,3,5,5)
print(a)
b=len(a)
print(b)


n=("a","b","c",["x","y"])  #可以修改元组中列表的值
n[3][0]="c"
n[3][1]="d"
print(n)

#字典

i={"qqq":12,"aaa":34,"zzz":56}
print(i)
for key in i.keys():
    print(key)

for value in i.values():
    print(value)
for j in i.items():
    print(j)

for key,value in i.items():
    print(key,value)

i["qqq"]=111
print(i)

i['cccc']=0000
print(i)

del(i["cccc"])
print(i)

i.clear()
print(id(i))
print(i)