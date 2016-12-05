import turtle

bob = turtle.Turtle()
print(bob)


def square(bob):
    for i in range(4):
       bob.fd(100)
       bob.lt(90)

def polygon(bob,n,side):
    for i in range(n):
       bob.fd(side)
       bob.lt(360/n)

square(bob)

side = 100
#turtle.colormode(255)

for i in range(6,10):
  #turtle.pencolor(0+i*10,0+i*10,0+i*10)
  bob.color('red')
  polygon(bob,i,side+i)

turtle.mainloop()

