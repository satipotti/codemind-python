n=int(input())
z=list(map(int,input().split()))
x=int(input())
f=0
for i in range(len(z)):
    if x==z[i]:
        f+=1
if f>0:
    print(f)
else:
    print('0')