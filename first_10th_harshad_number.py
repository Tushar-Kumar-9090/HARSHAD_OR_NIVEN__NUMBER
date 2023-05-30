
## WAP to print first 10th harshad number

t=int(input("Enter how many harshad/niven number you want: "))
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
        print(n)
    if c==t:
        break
    n+=1