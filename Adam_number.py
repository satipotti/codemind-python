n=int(input())
a=n*n
s=0
b=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
b=s*s
c=0
while b>0:
    m=b%10
    c=c*10+m
    b=b//10
if a==c:
    print('True')
else:
    print('False')