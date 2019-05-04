x=1
while x<10:
    y=1
    while y<=x:
        print ('%d*%d=%d'%(y,x,y*x),end="\t")
        if x==y:
            print ()
        y+=1
    x+=1