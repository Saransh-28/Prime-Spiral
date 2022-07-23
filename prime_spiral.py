# import all the required module
import turtle
from math import sqrt

# used turtle to draw on the screen
t = turtle.Turtle()
t.screen.bgcolor('black')
t.color('white')
t.pensize(1)
t.penup()
t.setpos(0,0)
t.pendown()

# check if the number is prime
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

#  take a left turn
def turn():
    t.left(90)

#  draw the dot when the number is prime , draw takes 2 arguments size=size of dot , step=distance between 2 numbers
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
        
# steps occurs in sequence [1,1,2,2,3,3,4,4 ....] so used flag variable to increment the numStep variable
        if flag%2 == 1:
            numSteps = numSteps + 1
        flag = flag + 1
        
draw()
