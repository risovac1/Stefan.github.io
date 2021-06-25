def fizzbuzz(a):
    m=1
    while(m<a):
        m+=1
        if(m%3==0):
            print("Fizz")
        elif(m%5==0):
            print("Buzz")
        elif(m%3==0 and m%5==0):   
             print("FizzBuzz")
        else:
             print(m)    

fizzbuzz(1000)    