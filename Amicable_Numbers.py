a=int(input())
b=int(input())
f_a=f_b=0
for i in range(1,a):
    if a%i==0:
        f_a+=i
for i in range(1,b):
    if b%i==0:
        f_b+=i
if f_a==b and f_b==a:
    print('Amicable')
else:
    print('Not Amicable')