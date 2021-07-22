from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():

    
    return render_template('home.html')



@app.route('/FizzBuzz/<int:count_to>')
def count(count_to):
    l=[]
    i=1
    while i<=count_to:     
        if(i%3==0):
            l.append("Fizz")
        elif(i%5==0):
            l.append("Buzz")
        elif(i%3==0 and i%5==0):   
             l.append("FizzBuzz")
        else:
           { l.append(i)}
        i+=1
    return render_template('FizzBuzz.html',numbers=l)