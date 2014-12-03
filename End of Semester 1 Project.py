from Tkinter import *
root = Tk()
drawpad = Canvas(width=1360,height=700, background='#BFF5ED')

#File retrieval (not being used at the moment)

#Background image
bg = PhotoImage(file = 'C:\Users\e134126\Documents\GitHub\\test\\Game BG.gif')
drawpad.create_image(0, 0, image = bg, anchor= NW)

#Player image
pimg = PhotoImage(file = 'C:\Users\e134126\Documents\GitHub\\test\\Player.gif')
player = drawpad.create_image(50, 100, image = pimg, anchor= NW)

#Projectile
blood = drawpad.create_rectangle(400,585,405,590, fill="black")

#Enemy image
enemy = drawpad.create_rectangle(50,50,100,60, fill="red", outline="red")

bloodfired = False
direction = 5
directon2 = -1

class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        self.bloodfired = False
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
        
    
    
    def animate(self):
        global drawpad
        global enemy
        global direction2
        global direction
        global bloodfired
        global player
        x1,y1,x2,y2 = drawpad.coords(enemy)
        rx1,ry1,rx2,ry2 = drawpad.coords(blood)

        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        
        if bloodfired == True:
            drawpad.move(blood, 10, 0)
        if self.collisionDetect() == True:
            drawpad.delete(enemy)
        if ry2<0:
            bloodfired = False
            drawpad.move(blood, (px1-rx1), (py1-ry1))
        #drawpad.after(10,self.animate)

    def key(self, event):
        global player
        global drawpad
        global blood
        print "hello"
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
        x1,y1,x2,y2 = drawpad.coords(enemy)
        if (rx1>=x1 and rx2<=x2) and (ry1>=y1 and ry2<=y2):
            return True
        else:
            return False
            
app = myApp(root)

#For canvas
root.mainloop()