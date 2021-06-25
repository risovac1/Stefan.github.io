def big_fibonacci(a):
    pom1=1
    
    y=1
    x=pow(10,a-1)
    
    while(y<=x):
        pom=y
        y=y+pom1
        pom1=pom

    print(y)       
       
big_fibonacci(3)
