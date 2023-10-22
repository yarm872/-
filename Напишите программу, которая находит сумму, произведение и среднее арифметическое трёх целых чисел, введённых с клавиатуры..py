a,b,c=map(int,input().split())
print(a,'+',b,'+',c,'=',a+b+c,sep='')
print(a,'*',b,'*',c,'=',a*b*c,sep='')
print('(',a,'+',b,'+',c,')/3=',"{:.3f}".format((a+b+c)/3),sep='')
