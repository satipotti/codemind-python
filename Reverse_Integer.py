n=int(input())
is_nagative=0
if n<0:
    is_nagative=1
    n=-n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if is_nagative==1:
    print(-rev)
else:
    print(rev)