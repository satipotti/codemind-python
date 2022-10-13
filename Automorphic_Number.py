n=int(input())
s=n*n
t=n
dc=0
while n>0:
    r=n%10
    dc=dc+1
    n=n//10
a=s%10**dc
if a==t:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')