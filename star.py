import pgzrun,random,time
WIDTH=500
HEIGHT=700
TITLE="Connecting stars"
star=[]
lines=[]
next_star=0
no_star=random.randint(5,10)
startTime=0
totalTime=0
endTime=0

def multiplication_table():
    for i in range(1, 11):  
         print(number,' x ', i, ' = ',number*i)

def create_star():
    global star, startTime
    for i in range(no_star):
        s=Actor("starr")
        s.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
        star.append(s)
        startTime=time.time()
create_star()
m=random.randint(2,9)
def draw():
    global totalTime
    screen.blit("spacee",(0,0))
    for i,s in enumerate(star):
        s.draw()
        screen.draw.text(str((i+1)*m),(s.pos[0],s.pos[1]+20))
    for i in lines:
        screen.draw.line(i[0],i[1],"white")
    if next_star < no_star:
        totalTime=time.time()-startTime
    screen.draw.text(str(round(totalTime,1)),(20,20),fontsize=30)
def update():
    pass

def on_mouse_down(pos):
    global next_star, lines
    if next_star < no_star:
        if star[next_star].collidepoint(pos):
            if next_star:
                lines.append((star[next_star-1].pos,star[next_star].pos))
            next_star = next_star+1
        else:
            lines=[]
            next_star=0





pgzrun.go()