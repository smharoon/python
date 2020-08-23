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
            pygame.draw.rect(win,(0,0,128),(temp.next.x1,temp.next.y1,10,10))
            temp.next=None
    def insertfirst(self,x1,y1,t):
        newnode=Node(x1,y1)
        if(self.head==None):
            self.head=newnode;
            newnode.next=None
        else:
            newnode.next=self.head
            self.head=newnode
            if t==6:
                pygame.draw.rect(win,(255,0,0),(newnode.x1,newnode.y1,10,10))
    

x=250
y=250
width=10
height=10 
vel=10
mylist=LinkedList()
a=1

j=randint(0,50)*10
k=randint(0,50)*10
run=True
run=False
pygame.draw.rect(win,(0,0,128),(50,50,400,400))
for i in range(20,26):
    pygame.draw.rect(win,(255,0,0),(x*10,250,width,height))
    mylist.insertfirst(i*10,250,6)
#print(x)
pygame.display.update()
while run==False:
    j=randint(6,42)*10
    k=randint(6,42)*10
    print(j,end=' ')
    print(k)
    run=mylist.traverse(j,k)
pygame.draw.rect(win,(255,255,255),(j,k,10,10))
pygame.display.update()
q=100
pygame.display.update()
while run==True:
    pygame.time.delay(q)
    keys=pygame.key.get_pressed()
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
        #print(2)
        x-=vel
    if a==3:
        y-=vel
    if a==4:
        y+=vel
    mylist.insertfirst(x,y,6)
    if mylist.head.x1==j and mylist.head.y1==k:
        pygame.draw.rect(win,(255,0,0),(j,k,10,10))
        q=q-5
        run=False
        while run==False:               #to check food does not get inside snake
            j=randint(6,42)*10
            k=randint(6,42)*10
            print(j,end=' ')
            print(k)
            run=mylist.traverse(j,k)
        pygame.draw.rect(win,(255,255,255),(j,k,10,10))
    else:
        mylist.deletelast()
    run=mylist.traverse(x,y)
    pygame.display.update()
    if(x<50 or x>450 or y<50 or y>450):
        run=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
pygame.quit()
