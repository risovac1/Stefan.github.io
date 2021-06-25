def is_prime(a):
    n=2
    x=0
    while(n<a):
        if(a%n==0):
            n=n+1
            x=1
        else:
            n=n+1
               
    if(x!=1):
        print("It is a prime number")
    else:
        print("It is not a prime number") 
    
is_prime(4)