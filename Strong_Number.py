sum=0   
num=int(input())    
temp=num    
while(num>0):    
    i=1    
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print('The number {} is a strong number'.format(temp))  
else:  
    print('The number {} is not a strong number'.format(temp))