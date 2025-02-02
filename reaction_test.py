import time as t
import pygame
import random
import sys


pygame.init()
screen = pygame.display.set_mode((1000, 600))

pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1000, 600))
pygame.display.update()
pygame.display.set_caption("Reaction Test")

def start_btn():
    pygame.draw.rect(screen, (255, 0, 0), (750, 50, 200, 100))
    pygame.display.update()


def lights():
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
  
    
def draw_board():
    for i in range(0, 600, 200):
        pygame.draw.rect(screen, (128, 128, 128), (50+i, 50, 150, 500))
        pygame.draw.rect(screen, (0, 0, 0), (50+i, 50, 150, 500), 3)
        for j in range(150, 600, 150):
            pygame.draw.circle(screen, (0, 0, 0), (125+i, j), 70)
    pygame.display.update()

def reset():
    start_btn()
    draw_board()


draw_board()
start_btn()


pxarray = pygame.PixelArray(screen)
turn = 0

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
            lights()
            print(event.pos)
            turn += 1
            
        elif event.type == pygame.MOUSEBUTTONDOWN and turn == 1:    
            if pxarray[538, 322] == screen.map_rgb(255, 0, 0):
                print("JUMPSTART!")
                pygame.event.clear()
            else:
                end = t.perf_counter()
                print(end - start)
            turn -= 1




            


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


        