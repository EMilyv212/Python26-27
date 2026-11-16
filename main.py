from myFunctions import *

c1 = 115 #Helpful for changing the binary code color whenever.
c2 = 160

bob.color(0,c1,0) #First
for times in range(7):
    jump(times*150-430,280)
    one(85, 10)
for times in range(6):
    jump(times*150-340,350)
    zero(35, 10)

bob.color(0,c2,0) #Second
for times in range(7):
    jump(times*150-430,240)
    zero(35, 10)
for times in range(6):
    jump(times*150-370,170)
    one(85, 10)

bob.color(0,c1,0) #Third
for times in range(7):
    jump(times*150-430,60)
    one(85, 10)
for times in range(6):
    jump(times*150-340,130)
    zero(35, 10)

bob.color(0,c2,0) #Fourth
for times in range(7):
    jump(times*150-430,20)
    zero(35, 10)
for times in range(6):
    jump(times*150-370,-50)
    one(85, 10)

bob.color(0,c1,0) #Fifth
for times in range(7):
    jump(times*150-430,-160)
    one(85, 10)
for times in range(6):
    jump(times*150-340,-90)
    zero(35, 10)

bob.color(0,c2,0) #Sixth
for times in range(7):
    jump(times*150-430,-200)
    zero(35, 10)
for times in range(6):
    jump(times*150-370,-270)
    one(85, 10)

bob.color(255,0,0) #Ring
for times in range(20):
    jump(times*2-280,times*2-155)
    rectangle(90,320,1)
for times in range(20):
    jump(times*2-190,times*2-245)
    rectangle(320,90,1)
for times in range(20):
    jump(times*2+130,times*2-155)
    rectangle(90,320,1)
for times in range(20):
    jump(times*2-190,times*2+165)
    rectangle(320,90,1)

jump(0,20)
bob.left(35)
bob.color(100,0,150) #Diamond
for times in range(70):
    diamond(30,80,4)
    bob.left(90)
    bob.forward(times*3)

jump(0,-380)
bob.color(255,0,0)
bob.write("I ' M  H E R E", align="center", font=("Times New Roman", 50, "normal"))
