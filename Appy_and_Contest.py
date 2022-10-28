n=int(input())
for _ in range(n):
    m,a,b,k=map(int,input().split())
    if (m//a)>=k or (m//b)>=k:
        print('Win')
    else:
        print('Lose')