from Tkinter import *
root = Tk()
drawpad = Canvas(width=1360,height=700, background='#BFF5ED')

import random
rand1 = random.randint(400,550)

#File retrieval (not being used at the moment)


#Background image
bg = PhotoImage(file = 'C:\Users\\Aubrey\\Documents\\GitHub\\End of Semester 1 Project\\End-of-Semester-1-Project\\Game BG.gif')
drawpad.create_image(0, 0, image = bg, anchor= NW)

#Projectile
blood = drawpad.create_oval(75,150,130,160, fill="red", outline="red")

#Player image
pimg = PhotoImage(file = 'C:\Users\\Aubrey\\Documents\\GitHub\\End of Semester 1 Project\\End-of-Semester-1-Project\\Player.gif')
player = drawpad.create_image(50, 100, image = pimg, anchor= NW)

#Enemy image
enmy = PhotoImage(file = 'C:\Users\\Aubrey\\Documents\\GitHub\\End of Semester 1 Project\\End-of-Semester-1-Project\\Enemy.gif')
enemy = drawpad.create_image(1300,rand1, image = enmy, anchor = NW)

playerhit = False
bloodfired = False
direction = 5
direction1 = -1
direction2 = 50

class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        self.bloodfired = False
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
        
    
    
    def animate(self):
        global drawpad
        global bloodfired
        global direction2
        global player
        global blood
        rx1,ry1,rx2,ry2 = drawpad.coords(blood)
        px1,py1 = drawpad.coords(player)
        
        if bloodfired == True:
            drawpad.move(blood, direction2, 0)
        if self.collisionDetect() == True:
            drawpad.delete(enemy)
            drawpad.move(blood, (px1-rx1) - 10, (py1-ry1) + 50)
        if rx1>1360:
            bloodfired = False
            drawpad.move(blood, (px1-rx1) - 20, (py1-ry1) + 50)  
        drawpad.after(10,self.animate)
        if self.collisionDetect2() == True:
            drawpad.delete(blood)
            drawpad.delete(player)
            print "You have died. Game over!"

    def key(self, event):
        global player
        global drawpad
        global blood
        global bloodfired
        x1,y1 = drawpad.coords(player)
        
        if event.char == " ":
            bloodfired = True
        if event.char == "w":
            if y1>0:
                drawpad.move(player,0,-50)
                drawpad.move(blood,0,-50)
        elif event.char == "d":
            if x1+50<800:
                drawpad.move(player,50,0)
                drawpad.move(blood,50,0)
        elif event.char == "a":
            if x1>0:
                drawpad.move(player,-50,0)
                drawpad.move(blood,-50,0)
        elif event.char == "s":
            if y1+100<600:
                drawpad.move(player,0,50)
                drawpad.move(blood,0,50)
            
    
    def collisionDetect(self):
        rx1,ry1,rx2,ry2 = drawpad.coords(blood)
        x1,y1 = drawpad.coords(enemy)
        if (rx1>=x1) and (ry1>=y1):
            return True
        else:
            return False
            
    def collisionDetect2(self):
        x1,y1 = drawpad.coords(player)
        ex1,ey1 = drawpad.coords(enemy)
        x2 = x1 + 106
        y2 = y1 +200
        if (ex1>=x1) and (ex1<=x2) and (ey1<=y1) and (ey1<=y2):
            return True
        else:
            return False

def animate1(): 
    global direction1
    global enemy
    x1, y1 = drawpad.coords(enemy)
    if x1 > drawpad.winfo_width():
        direction1 = -10
    elif x1 < -50:
        direction1 = 850
    drawpad.move(enemy,direction1,0)
    drawpad.after(10, animate1)   
        
          
animate1()   
app = myApp(root)

#For canvas
root.mainloop()