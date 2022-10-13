n = int(input())
b=n*n
a=b
s = 0
while a > 0: 
    r = a % 10 
    s = s+r
    a = a // 10
if n==s:
    print('Neon Number')
else:
    print('Not Neon Number')