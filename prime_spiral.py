import turtle
from math import sqrt

t = turtle.Turtle()

t.screen.bgcolor('black')
t.color('white')
t.pensize(1)
t.penup()
t.setpos(0,0)
t.pendown()

def isprime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def turn():
    t.left(90)

def draw(size=5,step=15):
    numSteps = 1
    flag = 0
    num = 1
    while True:
        
        for _ in range(numSteps):
            if isprime(num):
                t.dot(size)
            t.forward(step)
            num = num + 1
        turn()
        if flag%2 == 1:
            numSteps = numSteps + 1
        flag = flag + 1
        
draw()
