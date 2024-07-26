# Given the number 'n' , find out and return the number of digits in a number
n=int(input("Enter your number:"));
i=1
count=0
while(i<=n):
    d=n%10
    count=count+1
    n=n//10
print(count)
 