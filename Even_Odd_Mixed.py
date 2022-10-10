n = int(input()) # 124769
edc = odc = 0
while n > 0:
    r = n % 10
    if r%2 == 0:
        edc += 1
    else:
        odc += 1
    n = n // 10
if odc==0:
    print('Even')
elif edc==0:
    print('Odd')
else:
    print('Mixed')