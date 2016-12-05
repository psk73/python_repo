import turtle

side = 200
colors = ['red','yellow','green','blue','purple','orange']


def polyline(trtl,angle,nsteps,nlength,curv):
    '''
    Function to draw a arc
    '''
    for i in range(nsteps):
        trtl.fd(nlength/nsteps)
        if( curv == 'l'):
            trtl.lt(angle/nsteps)
        else:
            trtl.rt(angle/nsteps)


def drawFlower(bob,numPetals,petalAngle,petalDrawsteps,petalLength):
    '''
    Function to draw a flower
    '''
    for j in range(numPetals):
        bob.color(colors[j%len(colors)])
        polyline(bob,petalAngle,petalDrawsteps,petalLength,'l')
        bob.lt(180-petalAngle)
        polyline(bob,petalAngle,petalDrawsteps,petalLength,'l')
        bob.lt(180-petalAngle)
        bob.lt(360.0/numPetals)


def flowerApp():
    '''
    Application that draws flowers 
    '''
    bob = turtle.Turtle()
    bob.pensize(1)
    numFlowers = 20
    numPetals = 12
    petalAngle = 45
    petalDrawsteps = 4
    petalLength = 60
    xpos = 0
    ypos = 0
    indentSize = 0.7*petalLength
	numFlowersTemp=numFlowers
	numRound = 1
    for i in range(numFlowers
		numFlowersTemp-=1
        if i%4 == 0:
            signx= 1
            signy = 1
            xpos += indentSize
            ypos += indentSize
        elif i%4 == 1:
            signx = -1
            signy = 1
        elif i%4 == 2:
            signx = -1
            signy = -1
        elif i%4 == 3:
            signx = 1
            signy = -1
			numRound+=1

        bob.penup()
        bob.setpos(xpos*signx,ypos*signy)
        bob.pendown()
        drawFlower(bob,numPetals,petalAngle,petalDrawsteps,petalLength)

    turtle.mainloop()


if __name__ == '__main__':
    flowerApp()
