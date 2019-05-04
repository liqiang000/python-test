# x=1
# while x<10:
#     y=1
#     while y<=x:
#         print ('%d*%d=%d'%(y,x,y*x),end="\t")
#         if x==y:
#             print ()
#         y+=1
#     x+=1

# n=1
# i=0
# while n<=5:
#     m=1
#     while m<=n:
#         print ("*"*(i+1),end="")
#         if n==m:
#             print ()
#         m+=1
#     n+=1


# for i in range(1,6):
#     print("*"*i)

# for i in range(0,5):
#     for j in range(i+1):
#         if i==4:
#             print("*",end="")
#             continue
#         if j==0 or j==i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

for i in range(5):
    #print(i)
    print(" "*(4-i),end="")
    print("* "*(i+1))

