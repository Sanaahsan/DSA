# How to extract digits
n=float(input("Enter your number:"));
while(n>0):
    last_digit=n%10
    print(last_digit)
    n=n/10
