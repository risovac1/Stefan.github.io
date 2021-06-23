import math

def solve_quadratic(a,b,c):
    x=(-b+math.sqrt(pow(b,2)-4*a*c))/2*a
    y=(-b-math.sqrt(pow(b,2)-4*a*c))/2*a
    if(x!=y):
        print(x,y)
    elif(x==y):
        print(x)
    else:
        print('There is no solution')    




solve_quadratic(1,-5,6)   