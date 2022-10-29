t=int(input())
for _ in range(t):
    x=int(input())
    n=x
    while True:
        p=True
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                p=False
                break
        if p==True:
            break
        n+=1
    pp=x
    while True:
        p=True
        for i in range(2,int(pp**0.5)+1):
            if pp%i==0:
                p=False
                break
        if p==True:
            break
        pp-=1
    if x-pp<=n-x:
        print(pp)
    else:
        print(n)