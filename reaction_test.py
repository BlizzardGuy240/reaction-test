import time as t
import pygame
import random
import sys

l = []

pygame.init()
screen = pygame.display.set_mode((650, 700))

pygame.draw.rect(screen, (255, 255, 255), (0, 0, 650, 700)) #1000, 600
pygame.display.update()
pygame.display.set_caption("Reaction Test")

for k in range(100, 500):
    l += [k/100]



def lights():
    draw_board()
    for i in range(0, 600, 200):
        pygame.draw.circle(screen, (255, 0, 0), (125+i, 150), 70)
        pygame.draw.circle(screen, (255, 0, 0), (125+i, 300), 70)
        pygame.draw.circle(screen, (255, 0, 0), (125+i, 450), 70)
        if i != 0:
            t.sleep(1)
        pygame.display.update()
    t.sleep(random.choice(l))
    draw_board()
    global start
    start = t.perf_counter()
    global turn
    turn += 1
    

    
def draw_board():
    for i in range(0, 600, 200):
        pygame.draw.rect(screen, (128, 128, 128), (50+i, 50, 150, 500))
        pygame.draw.rect(screen, (0, 0, 0), (50+i, 50, 150, 500), 3)
        for j in range(150, 600, 150):
            pygame.draw.circle(screen, (0, 0, 0), (125+i, j), 70)
    pygame.display.update()



draw_board()
l1 = []
l2 = []


turn = 0

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN and turn == 0 and len(l1) == 0:
            print(event.pos)
            pygame.draw.rect(screen, (255, 255, 255), (0, 500, 1000, 1000))
            lights()
            pygame.event.clear()
            l1 += [1]
            # if event.type == pygame.MOUSEBUTTONDOWN and turn == 1 and len(l1) == 1:
            #     print("jumpstart")
            #     pygame.event.clear()
            #     del l1[0]
            #     break
            
            
        elif event.type == pygame.MOUSEBUTTONDOWN and turn == 1 and len(l1) == 1:
            del l1[0]
            global end
            end = t.perf_counter()
            a = (end - start)
            print(a)
            time = pygame.font.SysFont("freesansbold.ttf", 100).render(str("{:.2f}".format(a*1000)) + 'ms', 1, (0, 0, 0))
            screen.blit(time, (175, 580))
            pygame.display.update()
            turn -= 1
            l2 += ["{:.2f}".format(a*1000)]




            


            # for i in range(750, 950):
            #     for j in range(50, 150):
            #         if event.pos == (i, j) and pxarray[i, j] == screen.map_rgb(255, 0, 0):
            #             lights()
            #             pygame.event.clear()
            #             if pxarray[125, 150] == screen.map_rgb(0, 0, 0):
            #                 end = t.perf_counter()
            #                 print(end - start)

                            
                            
                        
                    
            # if event.type == pygame.MOUSEBUTTONDOWN and turn == 1:
            #     reset()
            #     turn = turn % 2
                        
                    
                        
                        
            # if pxarray[400+125,300] == screen.map_rgb(255, 0, 0):
            #     pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
            #     if event.type == pygame.MOUSEBUTTONDOWN:
            #         draw_board()
            # print(event.type)
            # pass


        