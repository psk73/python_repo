import turtle
import math

side = 200
colors = ['red','yellow','green','blue','purple','orange']


def polyline(trtl,angle,nsteps,nlength,curv):
    '''
    Function that can draw arc either curving to left or right
    '''
    for i in range(nsteps):
        trtl.fd(nlength/nsteps)
        if( curv == 'l'):
            trtl.lt(angle/nsteps)
        else:
            trtl.rt(angle/nsteps)


def drawFlower(bob,numPetals,petalAngle,petalDrawsteps,petalLength):
    '''
    Function that can draws a flower with given number of petals
    '''
    bob.circle(0.1*petalLength)
    for j in range(numPetals):
        bob.color(colors[j%len(colors)])
        polyline(bob,petalAngle,petalDrawsteps,petalLength,'l')
        bob.lt(180-petalAngle)
        polyline(bob,petalAngle,petalDrawsteps,petalLength,'l')
        bob.lt(180-petalAngle)
        bob.lt(360.0/numPetals)

def drawFlowerD(bob,numPetals,petalAngle,petalDrawsteps,petalLength):
    print "Test drawflower"
    
def calculateFlowerPositions(numFlowers, indentSize):
    temp = numFlowers
    i = 1
    while (temp > 0):
        temp = temp -4*i
        if temp >0:
            i+=1
        else:
            break
    #print "NumFlowers = ", numFlowers
    #print "Max flowers per round = ", i  
    posList = []
    for m in range(i):
        radius = (m+1)*indentSize
        angle = 360.0/(4*(m+1))
        #print "round = ", m, " radius = ", radius, " angle = ", angle
        for n in range(4*(m+1)):
            theta = math.radians(n*angle)
            #print "theta = ", theta
            xpos = math.ceil(radius*math.sin(theta))
            ypos = math.ceil(radius*math.cos(theta))
            #print " sin = ", math.sin(theta), " cos = ", math.cos(theta)
            posList.append((xpos,ypos))
            
    #print "Calculated ", len(posList),"positions\n"
    #print "*"*15
    strToprint = " "
    for x,y in posList:
        strToprint += "(" + str(x)+ " " + str(y)+") "
    #print strTo#print, "\n", "-"*15
    return posList

def drawAxis(bob):
    bob.penup()
    bob.setpos(-300,0)
    bob.pendown()
    bob.fd(600)
    bob.penup()
    bob.setpos(0,-300)
    bob.lt(90)
    bob.pendown()
    bob.fd(600)
    bob.penup()
    bob.setpos(0,0)
    bob.rt(90)
    bob.pendown()
    
    
def flowerApp():
    '''
    This application draws multiple flowers using turtle graphics
    '''
    bob = turtle.Turtle()
    bob.pensize(2)
    numFlowers = 64
    numPetals = 5
    petalAngle = 45
    petalDrawsteps = 2
    petalLength = 20
    xpos = 0
    ypos = 0
    indentSize = 1.5*petalLength
    numFlowersTemp=numFlowers

    posList = calculateFlowerPositions(numFlowers,indentSize)
    #print "positions available " ,  len(posList)

    for i in range(numFlowers):
        #print "Flower # ", i
        xpos,ypos = posList[i]
        bob.penup()
        bob.setpos(xpos,ypos)
        #print "setting position " , xpos, " ", ypos
        bob.pendown()
        drawFlower(bob,numPetals,petalAngle,petalDrawsteps,petalLength)
        
    turtle.mainloop()


if __name__ == '__main__':
    flowerApp()
