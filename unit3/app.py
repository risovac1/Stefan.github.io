from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Monty Hall Game Show"
    
    text = """Let's say you are on a game show, and you have three doors in front of you A, B, and C. 
    Behind one you get one billion dollars other two de nada, good luck. """

    choices = [
        ('choose_A',"A"),
        ('choose_B',"B"),
        ('choose_C',"C")
    ]

    return render_template('MontyHall.html', title=title, text=text, choices=choices)



@app.route("/choosen_A")
def choose_A():
    title = "So you choose A."
    
    text = """Ok, I mean you have 33% to get it right. So i will help you out I will erase C. Which one do you choose. Choose wisely."""

    choices = [
        ('choose_A1',"A"),
        ('choose_B1',"B")
    ]

    return render_template('MontyHall.html', title=title, text=text, choices=choices)

@app.route("/choosen_B")
def choose_B():
    title = "So you choose B."
    
    text = """Ok, I mean you have 33% to get it right. So i will help you out I will erase A. Which one do you choose. Choose wisely."""

    choices = [
        ('choose_B2',"B"),
        ('choose_C1',"C")
    ]

    return render_template('MontyHall.html', title=title, text=text, choices=choices)

@app.route("/choosen_C")
def choose_C():
    title = "So you choose C."
    
    text = """Ok, I mean you have 33% to get it right. So i will help you out I will erase B. Which one do you choose. Choose wisely."""

    choices = [
        ('choose_A2',"A"),
        ('choose_C2',"C")
    ]

    return render_template('MontyHall.html', title=title, text=text, choices=choices)

@app.route("/choosen_C2")
def choose_C2():
    title = "So you choose C again!"
    
    text = """Well too bad, you get nothing. Bye, bye, better luck next time."""

    choices = []

    return render_template('MontyHall.html', title=title, text=text, choices=choices)

@app.route("/choosen_A2")
def choose_A2():
    title = "So you choose A!"
    
    text = """Tuturutu. We have a winer. Congratulations you are billionaire now, go and spend your money."""

    choices = []

    return render_template('MontyHall.html', title=title, text=text, choices=choices)

@app.route("/choosen_A1")
def choose_A1():
    title = "So you choose A again!"
    
    text = """Well too bad, you get nothing. Bye, bye, better luck next time."""

    choices = []

    return render_template('MontyHall.html', title=title, text=text, choices=choices)

@app.route("/choosen_B1")
def choose_B1():
    title = "So you choose B!"
    
    text = """Tuturutu. We have a winer. Congratulations you are billionaire now, go and spend your money."""

    choices = []

    return render_template('MontyHall.html', title=title, text=text, choices=choices)



@app.route("/choosen_B2")
def choose_B2():
    title = "So you choose B again."
    
    text = """Well too bad, you get nothing. Bye, bye, better luck next time."""

    choices = []

    return render_template('MontyHall.html', title=title, text=text, choices=choices)

@app.route("/choosen_C1")
def choose_C1():
    title = "So you choose C."
    
    text = """Tuturutu. We have a winer. Congratulations you are billionaire now, go and spend your money."""

    choices = []

    return render_template('MontyHall.html', title=title, text=text, choices=choices) 

