num=int(input())
m=0
while num>0:
    d=num%10
    if m<d:
        m=d
    num=num//10
print(m)