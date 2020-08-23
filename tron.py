import pygame
from random import randint
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("snake")
flag=1
run=True
class Node:
    def __init__(self,x1=None,y1=None):
        self.x1=x1
        self.y1=y1
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def traverse(self,u,v):
        if(self.head==None):
            print("error")
        else:
            temp=self.head
            while temp!=None:
                if(u==temp.x1 and v==temp.y1 and temp!=self.head):
                    run=False
                    return run
                temp=temp.next
            return True
    def deletelast(self):
        if(self.head==None):
            print("error")
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            pygame.draw.rect(win,(0,0,128),(temp.next.x1,temp.next.y1,width,height))
            temp.next=None
    def insertfirst(self,x1,y1,t):
        newnode=Node(x1,y1)
        if(self.head==None):
            self.head=newnode;
            newnode.next=None
        else:
            newnode.next=self.head
            self.head=newnode
            if t==1:
                pygame.draw.rect(win,(255,0,0),(newnode.x1,newnode.y1,width,height))
            else:
                pygame.draw.rect(win,(0,0,125),(newnode.x1,newnode.y1,width,height))
    

x=250
y=270
x2=250
y2=220
width=5
height=5 
vel=5
mylist=LinkedList()
mylist2=LinkedList()
a=1
run=True
pygame.draw.rect(win,(255,0,0),(250,270,width,height))
pygame.draw.rect(win,(0,0,125),(250,220,width,height))
mylist.insertfirst(250,220,1)
mylist2.insertfirst(25,270,2)
pygame.display.update()
q=50
pygame.display.update()
b=1
while run==True and mylist.traverse(x2,y2) and mylist2.traverse(x,y):
    pygame.time.delay(q)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_p]:
        print(1)
        t=1
        while t==1:
            if keys[pygame.K_p]:
                run=False
    if keys[pygame.K_LEFT] and a!=1:
        a=2
    if keys[pygame.K_RIGHT] and a!=2:
        a=1
    if keys[pygame.K_UP] and a!=4:
        a=3
    if keys[pygame.K_DOWN] and a!=3:
        a=4 
    if a==1:
        x+=vel
    if a==2:
        x-=vel
    if a==3:
        y-=vel
    if a==4:
        y+=vel
    mylist.insertfirst(x,y,1)

    if keys[pygame.K_a] and b!=1:
        b=2
    if keys[pygame.K_d] and b!=2:
        b=1
    if keys[pygame.K_w] and b!=4:
        b=3
    if keys[pygame.K_s] and b!=3:
        b=4 
    if b==1:
        x2+=vel
    if b==2:
        x2-=vel
    if b==3:
        y2-=vel
    if b==4:
        y2+=vel
    mylist2.insertfirst(x2,y2,2)
    
    pygame.display.update()
    if(x<1 or x>500 or y<1 or y>500 or x2<1 or x2>500 or y2>500 or y2<1):
        run=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
pygame.quit()
popup=tk.Tk()
def leavemini():
    popup.destroy()
popup.wm_title("!")
label=ttk.Label(popup,text=msg,font=NORM_FONT)
label.pack(side="top",fill="x",pady=10)
B1=ttk.Button(popup,text="Okay",command=leavemini)
B1.pack()
popup.mainloop()
