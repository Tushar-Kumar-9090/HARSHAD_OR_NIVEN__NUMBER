
## WAP to print 10th harshad number???
#! Dynamically

t=int(input("Enter which placed harshad/niven number you want: "))
n=1
c=0
while True:
    num=n
    sum=0
    while num>0:
        rem=num%10
        sum+=rem
        num=num//10
    if n%sum==0:
        c+=1
    if c==t:
        print(n)
        break
    n+=1