import math

def solve_quadratic(a,b,c):
    z=pow(b,2)-4*a*c
    if(z>=0):
       
        x=(-b+math.sqrt(z))/2*a
        y=(-b-math.sqrt(z))/2*a
        if(x!=y):
            print(x,y)
        elif(x==y):
            print(x)
    else:
        print('There is no result')    




solve_quadratic(1,0,1)   