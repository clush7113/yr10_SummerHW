import pygame, sys #imports pygame library and sys module into code

pygame.init()      #initializes all python modules

screen = pygame.display.set_mode([225,150]) #sets display screen to size of sprite

b=pygame.Color("blue") #condenses colours down to single letters for ease of use
w=pygame.Color("white")

sprite=[ #defines sprite as 2d list of coloured pixels
    [w,w,b,b,b,b,b,w,w],
    [w,w,b,w,b,w,b,w,w],
    [w,w,b,b,b,b,b,w,w],
    [w,b,b,b,w,b,b,b,w],
    [b,w,w,b,b,b,w,w,b],
    [b,b,w,w,w,w,w,b,b],
    ]

for y,row in enumerate(sprite): #goes over each pixel and prints it into screen
    for x, colour in enumerate(row):
        rect = pygame.Rect(x*25,y*25,25,25)
        screen.fill(colour,rect=rect)

pygame.display.update() #update the display screen with sprite

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
