
## Given Number is Harshad//Niven Number or not??

n=int(input("Enter n value: "))
num=n
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n=n//10
if num%sum==0:
    print("harshasd number")
else:
    print("not harshad number")
