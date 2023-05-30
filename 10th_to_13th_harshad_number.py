
## WAP to print 10th to 13th harshad number???

n=1
c=0
ll=int(input("Enter lower level number: "))
ul=int(input("Enter lower upper number: "))
while True:
    num=n
    sum=0
    while num>0:
        rem=num%10
        sum+=rem
        num=num//10
    if n%sum==0:
        c+=1
        if c>=ll:
            print(n)
    if c==ul:
        break
    n+=1

