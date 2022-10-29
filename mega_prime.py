n=int(input())
p=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        p=False
        break
d=True
while n>0:
    r=n%10
    if r!=2 and r!=3 and r!=5 and r!=7:
        d=False
        break
    n=n//10
if p and d:
    print('Mega Prime')
else:
    print('Not Mega Prime')