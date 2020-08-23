import pygame
import math
import random
pygame.init()
win=pygame.display.set_mode((200,320))
pygame.display.set_caption("Tetris")

x=0
y=0
width=20
height=20
vel=4
cu=0
cl=0
cr=0

s1=[[0,1,1],
    [1,1,0]]
s2=[[1,0],
    [1,1],
    [0,1]]

l1=[[0,0,1],
    [1,1,1]]
l2=[[1,0],
    [1,0],
    [1,1]]
l3=[[1,1,1],
    [1,0,0]]
l4=[[1,1],
    [0,1],
    [0,1],
    [0,1]]

z1=[[1,1,0],
    [0,1,1]]
z2=[[0,1],
    [1,1],
    [1,0]]

j1=[[1,0,0],
    [1,1,1]]
j2=[[1,1],
    [1,0],
    [1,0],
    [1,0]]
j3=[[1,1,1],
    [0,0,1]]
j4=[[0,1],
    [0,1],
    [0,1],
    [1,1]]

o1=[[1,1],
    [1,1]]

i1=[[1,1,1,1]]
i2=[[1],
    [1],
    [1],
    [1]]

t1=[[1,1,1],
    [0,1,0]]
t2=[[0,1],
    [1,1],
    [0,1]]
t3=[[0,1,0],
    [1,1,1]]
t4=[[1,0],
    [1,1],
    [1,0]]

sshape=[s1,s2]
tshape=[t1,t2,t3,t4]
lshape=[l1,l2,l3,l4]
jshape=[j1,j2,j3,j4]
ishape=[i1,i2]
oshape=[o1]
zshape=[z1,z2]
rot=0
#print(random.randint(0,5))
run= True
pygame.display.update()
pi=[[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]
rand=[sshape,lshape,ishape,zshape,oshape,tshape,jshape]
xx=random.randint(0,6)
t=rand[xx]
stopxl=False
stopxr=False
gg=[[0, 200, 0],
    [0, 0, 128],
    [0, 255, 0],
    [200, 0, 0],
    [102, 0, 102],
    [255, 100, 100],
    [153, 0, 153]]
stop=False
while run:
    pygame.time.delay(100)
    rotlen=len(t)
    #print(rot)
    temp=t[rot]
    rows = len(temp)
    columns = len(temp[0])
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x>0 and stopxl==False:
                x-=20
            if event.key==pygame.K_RIGHT and x<200-20*columns and stopxr==False:
                x+=20
            if event.key==pygame.K_UP and stopxl==False and stopxr==False:
                if rot==rotlen-1:
                    rot=0
                else:
                    rot+=1
    if keys[pygame.K_DOWN]and y<300:
        y+=vel
    #y+=1
    if y<320-20*rows:
        y=y+4
    stopxl=False
    stopxr=False

    if x+20*columns>200:
        x=200-20*columns

    win.fill((0,0,0))
    for i in range(rows):
        for j in range(columns):
            if temp[i][j]==1:
                #print ("f")
                pygame.draw.rect(win,gg[xx],(x+20*j,y+20*i,width,height))
                

    #win.fill((0,0,0))
    for k in range(16):
        for l in range(10):
            if pi[k][l]!=0:
                pygame.draw.rect(win,gg[pi[k][l]-1],(l*20,k*20,width,height))


    
    for i in range(15):
        fill=True
        #print(15-i)
        for j in range(10):
            if pi[15-i][j]==0:
                fill=False
        if fill==True:
            vel=vel+1
            k=15-i
            while k>0:
                pi[k]=pi[k-1]
                k-=1
            pi[k]=[0,0,0,0,0,0,0,0,0,0]

    for i in range(rows):                       
        yo=math.ceil(y/20)*20
        for j in range(columns):
            yy=y+20*i
            aa=math.floor(yy/20)
            bb=math.floor(x/20)
            if temp[i][j]==1 and y<320-20*rows and bb+j<10:
                if pi[aa+1][bb+j]!=0:
                    stop=True
            if temp[i][j]==1 and x>0 and x<200-20*columns:
                if pi[math.floor((yo+20*i)/20)][math.floor((x+20*j)/20)-1]!=0:
                    stopxl=True
                if pi[math.floor((yo+20*i)/20)][math.floor((x+20*j)/20)+1]!=0:
                    stopxr=True

    for i in range(10):
        if pi[0][i]!=0:
            run=False
    if y>320-20*rows-1 or stop==True:
        #print(temp[rows-1])
        
        u=math.floor(x/20)
        v=math.floor(y/20)
        uu=u
        #print(v,u)
        for i in range(rows):
            u=uu
            for j in range(columns):
                #print(i,j,v,u)
                if temp[i][j]==1:
                    pi[v][u]=xx+1
                u+=1
            v+=1
        xx=random.randint(0,6)
        t=rand[xx]
        rot=0
        x=0
        y=0
        stop=False
    pygame.display.update()
    
pygame.quit()
