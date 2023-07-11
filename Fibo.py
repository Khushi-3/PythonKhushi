n=int(input("Enter the number for which you wish to calculate the Fibonacci Series:"))
def Fibo(n):
    if n<0:
        print("please enter valid inputs");
    elif n==0:
        return 0;
    elif n==1 or n==2:
        return 1;
    else:
        return Fibo(n-1)+Fibo(n-2)

print(Fibo(n))
        
